#!/usr/bin/env python
from __future__ import print_function, division

# This sample script connects to the AIWolf server
# and responds appropriately to all server requests.
# It does not say anything and gives itself as the
# target id for any request, resulting in random actions.

# Additionally, it prints to the standard input all the
# information that it received from the server, which can
# be useful when developing your own client.

import aiwolfpy
import aiwolfpy.contentbuilder as cb
import logging, json
from random import randint

# If we run multiple instance of this agent, it is good if
# Each instance has a different name. In a contest setting,
# You don't want to do this.
myname = 'omgus{:02d}'.format(randint(0,99))

class SampleAgent(object):
    def __init__(self, agent_name):
        # myname
        self.myname = agent_name
        logging.basicConfig(filename=self.myname+".log",
                            level=logging.DEBUG,
                            format='')

    def getName(self):
        return self.myname

    def initialize(self, base_info, diff_data, game_setting):
        # New game init:
        # Store my own ID:
        self.myid = base_info["agentIdx"]
        logging.debug("# INIT: I am agent {}".format(self.myid))
        self.player_total = game_setting["playerNum"]

        # Initialize a list with the hate score for each player
        # Also reduce own-hate score by 10k
        self.player_score = [0]*self.player_total
        self.player_score[self.myid-1] = -10000

        # the hate attribute contains the player ID that I hate the most.
        self.hate = self.player_score.index(max(self.player_score)) + 1

    # I will vote, attack and divine the most hated player so far.
    def vote(self):
        logging.debug("# VOTE: "+str(self.hate))
        return self.hate

    def attack(self):
        logging.debug("# ATTACK: "+str(self.hate))
        return self.hate

    def divine(self):
        logging.debug("# DIVINE: "+str(self.hate))
        return self.hate



    # new information (no return)
    def update(self, base_info, diff_data, request):
        logging.debug("# UPDATE")

        # At the beginning of the day, reduce score of dead players
        if (request == "DAILY_INITIALIZE"):
            for i in range(self.player_total):
                if (base_info["statusMap"][str(i+1)] == "DEAD"):
                    self.player_score[i] -= 10000

        # Check each line in Diff Data for talks or votes
        # logging.debug(diff_data)
        for row in diff_data.itertuples():
            type = getattr(row,"type")
            text = getattr(row,"text")
            if (type == "vote"):
                voter = getattr(row,"idx")
                target = getattr(row,"agent")
                if target == self.myid:
                    # They voted for me!
                    logging.debug("Agent {} voted for me!".format(voter))
                    self.player_score[voter-1] += 100
            elif (type == "talk" and "[{:02d}]".format(self.myid) in text):
                # they are talking about me
                source = getattr(row,"agent")
                logging.debug("Talking about me: {}".format(text))
                if "WEREWOLF" in text or "VOTE" in text:
                    # Are you calling me a werewolf!?
                    # Are you threateningto vote me?
                    self.player_score[source-1] += 10
                else:
                    # Stop talking about me!
                    self.player_score[source-1] += 1

        # Print Current Hate list:
        self.hate = self.player_score.index(max(self.player_score)) + 1
        logging.debug("Hate Score: "+", ".join(str(x) for x in self.player_score))

    # Start of the day (no return)
    def dayStart(self):
        logging.debug("# DAYSTART")
        return None

    # conversation actions: require a properly formatted
    # protocol string as the return.
    def talk(self):
        logging.debug("# TALK")

        # We just cycle through these three accusing messages
        # We can probably do something smarter here.
        hatecycle = [
        "REQUEST ANY (VOTE Agent[{:02d}])",
        "ESTIMATE Agent[{:02d}] WEREWOLF",
        "VOTE Agent[{:02d}]",
        ]
        return hatecycle[randint(0,2)].format(self.hate)

    def whisper(self):
        logging.debug("# WHISPER")
        # We just affirm the desire to attack the hated player
        # We can probably remove werewolves from hated player list in this case
        return "ATTACK Agent[{:02d}]".format(self.hate)


    def guard(self):
        logging.debug("# GUARD")
        return self.myid

    # Finish (no return)
    def finish(self):
        logging.debug("# FINISH")
        return None

agent = SampleAgent(myname)

# run
if __name__ == '__main__':
    aiwolfpy.connect_parse(agent)
