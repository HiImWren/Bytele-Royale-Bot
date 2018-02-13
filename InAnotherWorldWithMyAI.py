import random

from game.client.user_client import UserClient
from game.common.enums import *

TrapTimer=0;


class CustomClient(UserClient):


    class Node:
        def __init__(self):
            self.left = None
            self.right = None
            self.data = None



    def __init__(self):
        self.ItemNumber = 0;
        self.dungeonLevel = 0;
        # self.BrawlerLastHealthTurn = 0;
        # self.RogueLastHealthTurn = 0;
        # self.PikemanLastHealthTurn = 0;
        # self.KnightLastHealthTurn = 0;
        self.wizardTimer=3;
        """ Use the constructor to initialize any variables you would like to track between turns. """


    def team_name(self):
        print("Sending Team Name")

        return "AESTHETIC YUUSHA"

    def unit_choice(self):
        print("Sending Unit Choices")

        return [

                {
                    "name": "Mina",
                    "class": UnitClass.wizard
                },
                {
                    "name": "Yoshitsune",
                    "class": UnitClass.knight
                },
                {
                    "name": "Norn",
                    "class": UnitClass.pikeman
                },
                {
                    "name": "Metatron",
                    "class": UnitClass.rogue
                }
            ]


    def town(self, units, gold, store):
        self.dungeonLevel+=1
        print()
        print("*"*50)
        print("Town")
        print("*"*50)
        print("Dungeon Level" + str(self.dungeonLevel))
        print("Gold: {}".format(gold))
        Knight = None
        Brawler = None
        Pikeman = None
        Rogue = None
        Magus = None
        Wizard = None
        Sorcerer = None
        Alchemist = None


        for u in units:
            x = u.unit_class
            if x == UnitClass.knight:
                Knight = u
            if x == UnitClass.brawler:
                Brawler = u
            if x == UnitClass.pikeman:
                Pikeman = u
            if x == UnitClass.rogue:
                Rogue = u
            if x == UnitClass.magus:
                Magus = u
            if x == UnitClass.wizard:
                Wizard = u
            if x == UnitClass.sorcerer:
                Sorcerer = u
            if x == UnitClass.alchemist:
                Alchemist = u

        LastLength = len(store.purchases)
        HasMoney=True;
        store.items

        def GetCost(self,TheType,TheLevel):
            Cost = 0
            for item in store.items:

                if item.get("type")==TheType and item.get("level")==TheLevel:
                    return item.get("cost")
        runTimes = 0

        # if self.dungeonLevel==1:
        #     store.purchase(Knight, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Brawler, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Pikeman, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.armor, store.get_town_number() + 1)
        # if self.dungeonLevel==2:
        #     store.purchase(Rogue, ItemType.dagger, store.get_town_number() + 1)
        # if self.dungeonLevel==3:
        #     store.purchase(Knight, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.mace, store.get_town_number() + 1)
        #     store.purchase(Knight, ItemType.sword, store.get_town_number() + 1)
        #     store.purchase(Pikeman, ItemType.spear, store.get_town_number() + 1)
        # if self.dungeonLevel == 4:
        #     store.purchase(Pikeman, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.dagger, store.get_town_number() + 1)
        #
        # if self.dungeonLevel==5:
        #     store.purchase(Knight, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.mace, store.get_town_number() + 1)
        #     store.purchase(Knight, ItemType.sword, store.get_town_number() + 1)
        #     store.purchase(Pikeman, ItemType.spear, store.get_town_number() + 1)
        # if self.dungeonLevel == 6:
        #     store.purchase(Pikeman, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.dagger, store.get_town_number() + 1)
        # if self.dungeonLevel==7:
        #     store.purchase(Knight, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.mace, store.get_town_number() + 1)
        #     store.purchase(Knight, ItemType.sword, store.get_town_number() + 1)
        #     store.purchase(Pikeman, ItemType.spear, store.get_town_number() + 1)
        # if self.dungeonLevel == 8:
        #     store.purchase(Pikeman, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.dagger, store.get_town_number() + 1)
        # if self.dungeonLevel>9:
        #     store.purchase(Knight, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.armor, store.get_town_number())
        #     store.purchase(Brawler, ItemType.mace, store.get_town_number() + 1)
        #     store.purchase(Knight, ItemType.sword, store.get_town_number() + 1)
        #     store.purchase(Pikeman, ItemType.spear, store.get_town_number() + 1)
        #     store.purchase(Pikeman, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.armor, store.get_town_number() + 1)
        #     store.purchase(Rogue, ItemType.dagger, store.get_town_number() + 1)


        while HasMoney and runTimes<10:

            if(self.ItemNumber==0):
                gold = gold - GetCost(self,ItemType.armor,store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney=False;
                else:
                    store.purchase(Knight, ItemType.armor, store.get_town_number() + 1)
                    self.ItemNumber=self.ItemNumber+1
            if (self.ItemNumber == 1):
                gold = gold - GetCost(self, ItemType.wand, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Wizard, ItemType.wand, store.get_town_number() + 1)
                    self.ItemNumber = self.ItemNumber + 1
            if (self.ItemNumber == 2):
                gold = gold - GetCost(self,ItemType.spear, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Pikeman, ItemType.spear, store.get_town_number() + 1)
                    self.ItemNumber = self.ItemNumber + 1
            if (self.ItemNumber == 3):
                if self.dungeonLevel>7:
                    gold = gold - GetCost(self,ItemType.fire_bomb, store.get_town_number())*3
                    if gold <= 0:
                        HasMoney = False;
                    else:
                        self.ItemNumber += 1
                        print("WTF"+str(store.get_town_number()+1))
                        # for i in range(0,1):
                        store.purchase(Rogue, ItemType.fire_bomb,item_level=store.get_town_number(),item_slot=1)
                        store.purchase(Rogue, ItemType.shock_bomb, item_level=store.get_town_number(), item_slot=2)
                        store.purchase(Rogue, ItemType.frost_bomb, item_level=store.get_town_number(), item_slot=3)
                else: self.ItemNumber+=1
            if (self.ItemNumber == 4):
                gold = gold - GetCost(self,ItemType.armor, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Rogue, ItemType.armor, store.get_town_number() + 1)
                    self.ItemNumber = self.ItemNumber + 1
            if (self.ItemNumber == 5):
                gold = gold - GetCost(self,ItemType.sword, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Knight, ItemType.sword, store.get_town_number() + 1)
                    self.ItemNumber = self.ItemNumber + 1
            if (self.ItemNumber == 6):
                gold = gold - GetCost(self, ItemType.armor, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Wizard, ItemType.armor, store.get_town_number() + 1)
                    self.ItemNumber = self.ItemNumber + 1
            if (self.ItemNumber == 7):
                gold = gold - GetCost(self,ItemType.armor, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Pikeman, ItemType.armor, store.get_town_number() + 1)
                    self.ItemNumber = self.ItemNumber + 1
            if (self.ItemNumber == 8):
                gold = gold - GetCost(self,ItemType.dagger, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Rogue, ItemType.dagger, store.get_town_number() + 1)
                    self.ItemNumber +=1
            if (self.ItemNumber == 9):
                gold = gold - GetCost(self,ItemType.sword, store.get_town_number() + 1)
                if gold <= 0:
                    HasMoney = False;
                else:
                    store.purchase(Knight, ItemType.sword, store.get_town_number() + 1)
                    self.ItemNumber = 0
            runTimes+=1
    def room_choice(self, units, options):
        print(len(units))
        Knight = None
        Brawler = None
        Pikeman = None
        Rogue = None
        Magus = None
        Wizard = None
        Sorcerer = None
        Alchemist = None
        for u in units:
            x = u.unit_class
            if x == UnitClass.knight:
                Knight = u
            if x == UnitClass.brawler:
                Brawler = u
            if x == UnitClass.pikeman:
                Pikeman = u
            if x == UnitClass.rogue:
                Rogue = u
            if x == UnitClass.magus:
                Magus = u
            if x == UnitClass.wizard:
                Wizard = u
            if x == UnitClass.sorcerer:
                Sorcerer = u
            if x == UnitClass.alchemist:
                Alchemist = u
        global TrapTimer
        self.wizardTimer=3;
        TrapTimer=0
        curTotalHealth=0
        curDamagePerTurn=0
        curFocus=0
        curWill=0
        for u in units:
            curTotalHealth+=u.current_health
            curDamagePerTurn += (800 + self.dungeonLevel * 150)*u.current_health/u.health
            if u.current_health/u.health>0.2:
                curFocus+=u.focus
                curWill+=u.will
        # self.BrawlerLastHealthTurn =Brawler.current_health;
        # self.RogueLastHealthTurn = Rogue.current_health;
        # self.PikemanLastHealthTurn = Pikeman.current_health;
        # self.KnightLastHealthTurn = Knight.current_health;

        def TrapWeight(trap):
            if TrapType.eldritch_barrier:
                return 0
            if TrapType.spike_trap:
                return .99
            if TrapType.riddles_of_the_sphinx:
                if curWill > 45:
                    return 0
                if curWill > 30:
                    return 0
                else:
                    return -1
            if TrapType.puzzle_box:
                return 0
            if TrapType.pendulum_bridge:
                return 0
            if TrapType.falling_ceiling:
                if curWill > 45:
                    return 1
                if curWill > 30:
                    return 0
                else:
                    return -1
        if len(options) == 1:
            return Direction.forward
        if len(options.keys()) == 2:
            right = options[Direction.right]
            left = options[Direction.left]
            rightWeight = 1;
            leftWeight = 1;
            if right.node_type == NodeType.monster:
                monster = right.monster
                rightWeight = (curTotalHealth/monster.damage)-(monster.health/curDamagePerTurn)
            elif right.node_type == NodeType.trap:
                trap = right.trap
                rightWeight = TrapWeight(trap.trap_type)

            if left.node_type == NodeType.monster:
                monster = left.monster
                leftWeight = (curTotalHealth / monster.damage) - (monster.health / curDamagePerTurn)
            elif left.node_type == NodeType.trap:
                trap = left.trap
                leftWeight = TrapWeight(trap.trap_type)


            if leftWeight>=rightWeight:
                return Direction.left
            else:
                return Direction.right;

        else:
            return MessageType.null

    def combat_round(self, monster, units):
        print()
        print("*"*50)
        print("Combat")
        print("*"*50)
        print(monster.summary())
        Knight=None
        Brawler=None
        Pikeman=None
        Rogue=None
        Magus=None
        Wizard=None
        Sorcerer=None
        Alchemist=None
        TotalHealth=0
        TotalCurrentHealth=0;
        for u in units:
            TotalHealth= TotalHealth+u.health
            TotalCurrentHealth=TotalCurrentHealth+u.current_health

        for u in units:
            x = u.unit_class
            if x == UnitClass.knight:
                Knight = u
            if x == UnitClass.brawler:
                Brawler = u
            if x == UnitClass.pikeman:
                Pikeman = u
            if x == UnitClass.rogue:
                Rogue = u
            if x == UnitClass.magus:
                Magus = u
            if x == UnitClass.wizard:
                Wizard = u
            if x == UnitClass.sorcerer:
                Sorcerer = u
            if x == UnitClass.alchemist:
                Alchemist = u


        for u in units:
            print(u.summary())
        if Pikeman!=None:
            Pikeman.target_weakness()
        if Knight!=None:
            #if(Knight.current_health/Knight.health>=0.25 and TotalCurrentHealth/TotalHealth<0.5) or (Rogue!=None and Rogue.current_health/Rogue.health<=0.3):
            #    Knight.taunt()
            #else:
            if Knight.current_health<=.14:
                Knight.taunt()
            Knight.attack()
        # if Brawler!=None:
        #     #if(Brawler.current_health/Brawler.health >=0.3):
        #     #    Brawler.fit_of_rage()
        #     #else:
        #         if Brawler.current_health!=0 and Rogue.current_health!=0 and Brawler.current_health/self.BrawlerLastHealthTurn < Rogue.current_health/self.RogueLastHealthTurn and Pikeman.current_health!=0 and Brawler.current_health/self.BrawlerLastHealthTurn<Pikeman.current_health/self.PikemanLastHealthTurn and Knight.current_health!=0 and Brawler.current_health/self.BrawlerLastHealthTurn<Knight.current_health/self.KnightLastHealthTurn:
        #             Brawler.fit_of_rage()
        #         else:
        #             Brawler.attack()
        if Rogue!=None:
            Rogue.attack()
            if Rogue.bomb_1_quantity > 0:
                Rogue.use_bomb_1();
            if Rogue.bomb_2_quantity > 0:
                Rogue.use_bomb_2();
            if Rogue.bomb_2_quantity > 0:
                Rogue.use_bomb_2();
            for u in monster.weaknesses:
                if u == DamageType.fire and Rogue.bomb_1_quantity >0:
                    Rogue.use_bomb_1();
                    break
                if u == DamageType.electricity and Rogue.bomb_2_quantity >0:
                    Rogue.use_bomb_2();
                    break
                if u == DamageType.cold and Rogue.bomb_3_quantity >0:
                    Rogue.use_bomb_3();
                    break

        if Wizard!=None:
            if self.wizardTimer==3:
                Wizard.invigorate(Knight)
                self.wizardTimer=0
            else:
                Wizard.attack()
        self.wizardTimer+=1



        if Sorcerer!=None:
            Sorcerer.attack()
        if Magus!=None:
            Magus.elemental_burst()
        if Alchemist!=None:
            Alchemist.attack()

    def trap_round(self, trap, units):
        global TrapTimer
        print()
        print("*"*50)
        print("Trap!")
        print("*"*50)
        print(trap.summary())

        if trap.trap_type == TrapType.eldritch_barrier:
            for u in units:
                if u.current_focus <5:
                    u.trap_action = TrapAction.little_effort
                else:
                    u.trap_action = TrapAction.large_effort
        elif trap.trap_type == TrapType.falling_ceiling:
            for u in units:
                if u.current_will <5:
                    u.trap_action = TrapAction.little_effort
                else:
                    u.trap_action = TrapAction.large_effort
        elif trap.trap_type == TrapType.pendulum_bridge:
            if TrapTimer==3:
                for u in units:
                    u.trap_action = TrapAction.evade
                TrapTimer=0
            else:
                for u in units:
                    if u.current_will < 5:
                        u.trap_action = TrapAction.little_effort
                    else:
                        u.trap_action = TrapAction.large_effort
        elif trap.trap_type == TrapType.puzzle_box:
            minHealth = 99999999999999
            for u in units:
                if u.current_health < minHealth:
                    minHealth = u.current_health
            for u in units:
                if u.current_health == minHealth:
                    u.trap_action = TrapAction.evade
                else:
                    if u.current_focus < 5:
                        u.trap_action = TrapAction.little_effort
                    else:
                        u.trap_action = TrapAction.large_effort
        elif trap.trap_type == TrapType.riddles_of_the_sphinx:
            for u in units:
                if u.current_focus <5:
                    u.trap_action = TrapAction.little_effort
                else:
                    u.trap_action = TrapAction.large_effort
        elif trap.trap_type == TrapType.spike_trap:
            if TrapTimer==2:
                for u in units:
                    u.trap_action = TrapAction.evade
                TrapTimer=0
            else:
                for u in units:
                    if u.current_will < 5:
                        u.trap_action = TrapAction.little_effort
                    else:
                        u.trap_action = TrapAction.large_effort


        for u in units:
            print(u.summary())



        TrapTimer=TrapTimer+1


    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


