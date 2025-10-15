from otree.api import *
import random

doc = """
This file contains the full experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'main'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

likert_trust = [[1, "Tout à fait confiance"],[2, "Plutôt confiance"],
                [3, "Ni confiance, ni pas confiance"],[4, "Plutôt pas confiance"],
                [5, "Pas du tout confiance"]]
likert_agree = [[1, "Tout à fait d'accord"],[2, "Plutôt d'accord"],
                [3, "Ni d'accord, ni pas d'accord"],[4, "Plutôt en désaccord"],
                [5, "En complet désaccord"]]
class Player(BasePlayer):
    anon_id = models.StringField()
    location = models.StringField(initial="non-assigned",
                                      choices=[
                                        ["B", "Besançon"],
                                        ["INSP", "INSP"]])
    condition = models.StringField(initial="non-assigned")
    pgg_contrib = models.IntegerField(min=0, blank=True)
    pgg_beliefintra = models.FloatField(min=0, blank=True)
    pgg_beliefinteringroup = models.FloatField(min=0, blank=True)
    pgg_beliefinteroutgroup = models.FloatField(min=0, blank=True)
    tg_send = models.IntegerField(min=0, blank=True)
    dg_send = models.IntegerField(min=0, blank=True)
    tg_sendback1  = models.IntegerField(min=0, blank=True, label='Si vous recevez 3, combien renvoyez-vous ?')
    tg_sendback2  = models.IntegerField(min=0, blank=True, label='Si vous recevez 6, combien renvoyez-vous ?')
    tg_sendback3  = models.IntegerField(min=0, blank=True, label='Si vous recevez 9, combien renvoyez-vous ?')
    tg_sendback4  = models.IntegerField(min=0, blank=True, label='Si vous recevez 12, combien renvoyez-vous ?')
    tg_sendback5  = models.IntegerField(min=0, blank=True, label='Si vous recevez 15, combien renvoyez-vous ?')
    tg_sendback6  = models.IntegerField(min=0, blank=True, label='Si vous recevez 18, combien renvoyez-vous ?')
    tg_sendback7  = models.IntegerField(min=0, blank=True, label='Si vous recevez 21, combien renvoyez-vous ?')
    tg_sendback8  = models.IntegerField(min=0, blank=True, label='Si vous recevez 24, combien renvoyez-vous ?')
    tg_sendback9  = models.IntegerField(min=0, blank=True, label='Si vous recevez 27, combien renvoyez-vous ?')
    tg_sendback10 = models.IntegerField(min=0, blank=True, label='Si vous recevez 30, combien renvoyez-vous ?')
    tg_belief15 = models.IntegerField(min=0, blank=True, label='')
    tg_belief30 = models.IntegerField(min=0, blank=True, label='')

    # questionnaire
    quest_female = models.IntegerField(choices=[[1, "une femme"],
                                                [0, "un homme"],
                                                [-1, "autre/ne se prononce pas"]],
                                        label = "Vous êtes :")
    quest_birthyear = models.IntegerField(min=1900, max=2012, label="Quelle est votre année de naissance ?")
    quest_birthplace = models.StringField(label="Quel est votre pays de naissance ?")
    quest_study = models.IntegerField(choices=[[1, "Baccalauréat"],
                                                [2, "Licence et assimilé (bac +2/+3)"],
                                                [3, "Master et assimilé (bac +5)"],
                                                [4,"Doctorat et assimilé (bac +7 ou plus)"]],
                                      label = "Quel est votre niveau de diplôme le plus élevé ?")
    quest_trustgovernment   = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les membres du gouvernement")
    quest_trustparliament   = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les parlementaires")
    quest_trustlocal        = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les élus locaux")
    quest_trustcivilservant = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les fonctionnaires")
    quest_trustunions       = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les dirigeants syndicaux")
    quest_trustmedia        = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les médias")
    quest_trustscientist    = models.IntegerField(choices=likert_trust, widget=widgets.RadioSelect, label="Les scientifiques")
    quest_peoplecentrism1 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les responsables politiques et administratifs doivent toujours écouter attentivement les problèmes de la population.")
    quest_peoplecentrism2 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les responsables politiques et administratifs n'ont pas à passer du temps parmi les gens ordinaires pour faire du bon travail.")
    quest_antielitism1 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Le gouvernement est contrôlé par de grands intérêts privés pour leur propre bien.")
    quest_antielitism2 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les responsables politiques et administratifs utilisent leur pouvoir pour essayer d'améliorer la vie des gens.")
    quest_manicheism1 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les gens avec qui je ne suis pas d'accord politiquement ne sont pas malintentionnés.")
    quest_manicheism2 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les gens avec qui je ne suis pas d'accord politiquement sont simplement mal informés.")
    quest_expertise1 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les responsables politiques et administratifs doivent être comme des managers et réparer ce qui ne fonctionne pas dans la société.")
    quest_expertise2 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les problèmes sociaux doivent être traités en se fondant sur des preuves scientifiques, non des préférences idéologiques.")
    quest_antipolitics1 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les meilleures décisions politiques sont prises par les experts qui ne sont pas des politiciens.")
    quest_antipolitics2 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les politiciens veulent simplement promouvoir les intérêts de ceux qui votent pour eux et non l'intérêt de tout le pays.")
    quest_antipopulism1 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Les politiques devraient diriger le peuple, non le suivre.")
    quest_antipopulism2 = models.IntegerField(choices=likert_agree, widget=widgets.RadioSelect,label = "Aujourd'hui, les opinions des gens ordinaires sont déjà trop prises en compte, au détriment de l'intérêt général de long terme.")
    quest_generalinterest = models.IntegerField(choices=[[1,"L'intérêt général, c'est la somme des intérêts individuels."],
                                                        [2,"L'intérêt général, c'est l'intérêt du peuple."],
                                                        [3,"L'intérêt général, c'est l'intérêt de la Nation."],
                                                        [4,"L'intérêt général n'existe pas, il n'y a que des intérêts particuliers."],
                                                        ], label = "Parmi ces définitions de l'<strong>intérêt général</strong>, laquelle vous semble la meilleure (ou moins mauvaise) parmi celles proposées ?")
    round_pgg = models.IntegerField()
    round_dg = models.IntegerField()
    round_tg = models.IntegerField()
    
# note : set maximum in dynamic fields

# Functions

def Initialize(group):
    """
    Participants are randomly affected to two conditions :
    intra or inter. This is balanced between Besançon and Strasbourg
    """
    players = group.get_players()
    # Careful, location is random now, but we will have
    # to declare it.
    for p in players:
#        if p.round_number == 1:
            values = [1, 2, 3]
            random.shuffle(values)
            p.round_pgg = values[0]
            p.round_dg = values[1]
            p.round_tg = values[2]

            players_B= sorted([p for p in players if p.location == "B"],    key=lambda x: x.id_in_group)
            players_INSP = sorted([p for p in players if p.location == "INSP"], key=lambda x: x.id_in_group)

            for i, p in enumerate(players_B):
                p.condition = "Intra" if i % 2 == 0 else "Inter"

            for i, p in enumerate(players_INSP):
                p.condition = "Intra" if i % 2 == 0 else "Inter"

def Alert_Finish(group):
    print("Tout le monde a terminé de prendre ses décisions, le questionnaire s'affiche.")

# PAGES

class Initial_Location(Page):
    form_model = 'player'
    form_fields = ['location']
    def is_displayed(player):
        return player.round_number == 1

class Anon(Page):
    form_model = 'player'
    form_fields = ['anon_id']
    def error_message(player, values):
        if len(values['anon_id']) != 3 or not values['anon_id'][0].isalpha() or not values['anon_id'][1].isdigit() or not values['anon_id'][2].isdigit():
            return "Ce numéro d'anonymat ne semble pas valide, merci de le vérifier."

class GeneralInstructions(Page):
    def is_displayed(player):
        return player.round_number == 1
    
class WaitStart(WaitPage):
        wait_for_all_groups = True
        after_all_players_arrive = 'Initialize'


class DescriptionINSP(Page):
    def is_displayed(player):
        return player.condition == "Inter"


class Game1_1(Page):
    # Instructions for the first game.
    pass

class Simulator_TG1(Page):
    def is_displayed(player):
        return player.round_tg == 1

class Simulator_PGG1(Page):
    def is_displayed(player):
        return player.round_pgg == 1

class Simulator_DG1(Page):
    def is_displayed(player):
        return player.round_dg == 1

class Game1_2(Page):
    # Decision 1 for the first game
    form_model = 'player'
    form_fields = ['tg_send', 'dg_send','pgg_contrib']
    @staticmethod
    def error_message(player, values):
        if player.round_dg == 1 and values['dg_send'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_dg == 1 and values['dg_send']>20:
            return 'Le montant envoyé au participant B ne peut pas être au-delà de 10 ECUs.'
        if player.round_pgg == 1 and values['pgg_contrib'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_pgg == 1 and values['pgg_contrib']>20:
            return 'Le montant investi dans le compte collectif ne peut pas être au-delà de 20 ECUs.'
        if player.round_tg == 1 and values['tg_send'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_tg == 1 and values['tg_send']>10:
            return 'Le montant envoyé au participant B ne peut pas être au-delà de 10 ECUs.'

class Game1_3(Page):
    # Decision 2 for the first game if it is trust game.
    form_model = 'player'
    form_fields = ['tg_sendback1','tg_sendback2','tg_sendback3',
                   'tg_sendback4','tg_sendback5','tg_sendback6',
                   'tg_sendback7','tg_sendback8','tg_sendback9',
                   'tg_sendback10']
    @staticmethod
    def is_displayed(player):
        return player.round_tg == 1
    def error_message(player, values):
        if player.round_tg == 1 and values['tg_sendback1'] is None:
            return 'Merci de rentrer une valeur dans le premier champ.'
        elif player.round_tg == 1 and values['tg_sendback1']>3:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (3).'
        if player.round_tg == 1 and values['tg_sendback2'] is None:
            return 'Merci de rentrer une valeur dans le deuxième champ.'
        elif player.round_tg == 1 and values['tg_sendback2']>6:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (6).'
        if player.round_tg == 1 and values['tg_sendback3'] is None:
            return 'Merci de rentrer une valeur dans le troisième champ.'
        elif player.round_tg == 1 and values['tg_sendback3']>9:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (9).'
        if player.round_tg == 1 and values['tg_sendback4'] is None:
            return 'Merci de rentrer une valeur dans le quatrième champ.'
        elif player.round_tg == 1 and values['tg_sendback4']>12:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (12).'
        if player.round_tg == 1 and values['tg_sendback5'] is None:
            return 'Merci de rentrer une valeur dans le cinquième champ.'
        elif player.round_tg == 1 and values['tg_sendback5']>15:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (15).'
        if player.round_tg == 1 and values['tg_sendback6'] is None:
            return 'Merci de rentrer une valeur dans le sixième champ.'
        elif player.round_tg == 1 and values['tg_sendback6']>18:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (18).'
        if player.round_tg == 1 and values['tg_sendback7'] is None:
            return 'Merci de rentrer une valeur dans le septième champ.'
        elif player.round_tg == 1 and values['tg_sendback7']>21:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (21).'
        if player.round_tg == 1 and values['tg_sendback8'] is None:
            return 'Merci de rentrer une valeur dans le huitième champ.'
        elif player.round_tg == 1 and values['tg_sendback8']>24:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (24).'
        if player.round_tg == 1 and values['tg_sendback9'] is None:
            return 'Merci de rentrer une valeur dans le neuvième champ.'
        elif player.round_tg == 1 and values['tg_sendback9']>27:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (27).'
        if player.round_tg == 1 and values['tg_sendback10'] is None:
            return 'Merci de rentrer une valeur dans le dixième champ.'
        elif player.round_tg == 1 and values['tg_sendback10']>30:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (30).'

class Game1_4(Page):
    # Belief Elicitation for the first game if it is trust game or pgg.
    form_model = 'player'
    form_fields = ['pgg_beliefintra', 'pgg_beliefinteringroup', 'pgg_beliefinteroutgroup',
                    'tg_belief15', 'tg_belief30']
    @staticmethod
    def is_displayed(player):
        return player.round_tg == 1 or player.round_pgg == 1
    def error_message(player, values):
        if player.round_tg == 1 and values['tg_belief15'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_tg == 1 and values['tg_belief15']>15:
            return 'Le montant renvoyé ne peut pas être plus élevé que le montant reçu.'
        if player.round_tg == 1 and values['tg_belief30'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_tg == 1 and values['tg_belief30']>30:
            return 'Le montant renvoyé ne peut pas être plus élevé que le montant reçu.'        
        if player.round_pgg == 1 and player.condition == "Intra" and values['pgg_beliefintra'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 1 and player.condition == "Intra" and values['pgg_beliefintra']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."
        if player.round_pgg == 1 and player.condition == "Inter" and values['pgg_beliefinteringroup'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 1 and player.condition == "Inter" and values['pgg_beliefinteringroup']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."
        if player.round_pgg == 1 and player.condition == "Inter" and values['pgg_beliefinteroutgroup'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 1 and player.condition == "Inter" and values['pgg_beliefinteroutgroup']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."

class Game2_1(Page):
    # Instructions for the second game.
    pass

class Simulator_TG2(Page):
    def is_displayed(player):
        return player.round_tg == 2

class Simulator_PGG2(Page):
    def is_displayed(player):
        return player.round_pgg == 2

class Simulator_DG2(Page):
    def is_displayed(player):
        return player.round_dg == 2

class Game2_2(Page):
    # Decision 1 for the second game.
    form_model = 'player'
    form_fields = ['tg_send', 'dg_send','pgg_contrib']
    @staticmethod
    def error_message(player, values):
        if player.round_dg == 2 and values['dg_send'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_dg == 2 and values['dg_send']>20:
            return 'Le montant envoyé au participant B ne peut pas être au-delà de 10 ECUs.'
        if player.round_pgg == 2 and values['pgg_contrib'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_pgg == 2 and values['pgg_contrib']>20:
            return 'Le montant investi dans le compte collectif ne peut pas être au-delà de 20 ECUs.'
        if player.round_tg == 2 and values['tg_send'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_tg == 2 and values['tg_send']>10:
            return 'Le montant envoyé au participant B ne peut pas être au-delà de 10 ECUs.'

class Game2_3(Page):
    # Decision 2 for the second game if it is trust game.
    form_model = 'player'
    form_fields = ['tg_sendback1','tg_sendback2','tg_sendback3',
                   'tg_sendback4','tg_sendback5','tg_sendback6',
                   'tg_sendback7','tg_sendback8','tg_sendback9',
                   'tg_sendback10']
    @staticmethod
    def is_displayed(player):
        return player.round_tg == 2
    def error_message(player, values):
        if player.round_tg == 2 and values['tg_sendback1'] is None:
            return 'Merci de rentrer une valeur dans le premier champ.'
        elif player.round_tg == 2 and values['tg_sendback1']>3:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (3).'
        if player.round_tg == 2 and values['tg_sendback2'] is None:
            return 'Merci de rentrer une valeur dans le deuxième champ.'
        elif player.round_tg == 2 and values['tg_sendback2']>6:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (6).'
        if player.round_tg == 2 and values['tg_sendback3'] is None:
            return 'Merci de rentrer une valeur dans le troisième champ.'
        elif player.round_tg == 2 and values['tg_sendback3']>9:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (9).'
        if player.round_tg == 2 and values['tg_sendback4'] is None:
            return 'Merci de rentrer une valeur dans le quatrième champ.'
        elif player.round_tg == 2 and values['tg_sendback4']>12:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (12).'
        if player.round_tg == 2 and values['tg_sendback5'] is None:
            return 'Merci de rentrer une valeur dans le cinquième champ.'
        elif player.round_tg == 2 and values['tg_sendback5']>15:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (15).'
        if player.round_tg == 2 and values['tg_sendback6'] is None:
            return 'Merci de rentrer une valeur dans le sixième champ.'
        elif player.round_tg == 2 and values['tg_sendback6']>18:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (18).'
        if player.round_tg == 2 and values['tg_sendback7'] is None:
            return 'Merci de rentrer une valeur dans le septième champ.'
        elif player.round_tg == 2 and values['tg_sendback7']>21:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (21).'
        if player.round_tg == 2 and values['tg_sendback8'] is None:
            return 'Merci de rentrer une valeur dans le huitième champ.'
        elif player.round_tg == 2 and values['tg_sendback8']>24:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (24).'
        if player.round_tg == 2 and values['tg_sendback9'] is None:
            return 'Merci de rentrer une valeur dans le neuvième champ.'
        elif player.round_tg == 2 and values['tg_sendback9']>27:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (27).'
        if player.round_tg == 2 and values['tg_sendback10'] is None:
            return 'Merci de rentrer une valeur dans le dixième champ.'
        elif player.round_tg == 2 and values['tg_sendback10']>30:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (30).'

class Game2_4(Page):
    # Belief Elicitation for the first game if it is trust game or pgg.
    form_model = 'player'
    form_fields = ['pgg_beliefintra', 'pgg_beliefinteringroup', 'pgg_beliefinteroutgroup',
                    'tg_belief15', 'tg_belief30']
    @staticmethod
    def is_displayed(player):
        return player.round_tg == 2 or player.round_pgg == 2
    def error_message(player, values):
        if player.round_tg == 2 and values['tg_belief15'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_tg == 2 and values['tg_belief15']>15:
            return 'Le montant renvoyé ne peut pas être plus élevé que le montant reçu.'
        if player.round_tg == 2 and values['tg_belief30'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_tg == 2 and values['tg_belief30']>30:
            return 'Le montant renvoyé ne peut pas être plus élevé que le montant reçu.'        
        if player.round_pgg == 2 and player.condition == "Intra" and values['pgg_beliefintra'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 2 and player.condition == "Intra" and values['pgg_beliefintra']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."
        if player.round_pgg == 2 and player.condition == "Inter" and values['pgg_beliefinteringroup'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 2 and player.condition == "Inter" and values['pgg_beliefinteringroup']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."
        if player.round_pgg == 2 and player.condition == "Inter" and values['pgg_beliefinteroutgroup'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 2 and player.condition == "Inter" and values['pgg_beliefinteroutgroup']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."

class Game3_1(Page):
    # Instructions for the first game.
    pass

class Simulator_TG3(Page):
    def is_displayed(player):
        return player.round_tg == 3

class Simulator_PGG3(Page):
    def is_displayed(player):
        return player.round_pgg == 3

class Simulator_DG3(Page):
    def is_displayed(player):
        return player.round_dg == 3

class Game3_2(Page):
    # Decision 1 for the third game
    form_model = 'player'
    form_fields = ['tg_send', 'dg_send','pgg_contrib']
    @staticmethod
    def error_message(player, values):
        if player.round_dg == 3 and values['dg_send'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_dg == 3 and values['dg_send']>20:
            return 'Le montant envoyé au participant B ne peut pas être au-delà de 10 ECUs.'
        if player.round_pgg == 3 and values['pgg_contrib'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_pgg == 3 and values['pgg_contrib']>20:
            return 'Le montant investi dans le compte collectif ne peut pas être au-delà de 20 ECUs.'
        if player.round_tg == 3 and values['tg_send'] is None:
            return 'Merci de rentrer une valeur.'
        elif  player.round_tg == 3 and values['tg_send']>10:
            return 'Le montant envoyé au participant B ne peut pas être au-delà de 10 ECUs.'

class Game3_3(Page):
    # Decision 2 for the third game if it is trust game.
    form_model = 'player'
    form_fields = ['tg_sendback1','tg_sendback2','tg_sendback3',
                   'tg_sendback4','tg_sendback5','tg_sendback6',
                   'tg_sendback7','tg_sendback8','tg_sendback9',
                   'tg_sendback10']
    @staticmethod
    def is_displayed(player):
        return player.round_tg == 3
    def error_message(player, values):
        if player.round_tg == 3 and values['tg_sendback1'] is None:
            return 'Merci de rentrer une valeur dans le premier champ.'
        elif player.round_tg == 3 and values['tg_sendback1']>3:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (3).'
        if player.round_tg == 3 and values['tg_sendback2'] is None:
            return 'Merci de rentrer une valeur dans le deuxième champ.'
        elif player.round_tg == 3 and values['tg_sendback2']>6:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (6).'
        if player.round_tg == 3 and values['tg_sendback3'] is None:
            return 'Merci de rentrer une valeur dans le troisième champ.'
        elif player.round_tg == 3 and values['tg_sendback3']>9:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (9).'
        if player.round_tg == 3 and values['tg_sendback4'] is None:
            return 'Merci de rentrer une valeur dans le quatrième champ.'
        elif player.round_tg == 3 and values['tg_sendback4']>12:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (12).'
        if player.round_tg == 3 and values['tg_sendback5'] is None:
            return 'Merci de rentrer une valeur dans le cinquième champ.'
        elif player.round_tg == 3 and values['tg_sendback5']>15:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (15).'
        if player.round_tg == 3 and values['tg_sendback6'] is None:
            return 'Merci de rentrer une valeur dans le sixième champ.'
        elif player.round_tg == 3 and values['tg_sendback6']>18:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (18).'
        if player.round_tg == 3 and values['tg_sendback7'] is None:
            return 'Merci de rentrer une valeur dans le septième champ.'
        elif player.round_tg == 3 and values['tg_sendback7']>21:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (21).'
        if player.round_tg == 3 and values['tg_sendback8'] is None:
            return 'Merci de rentrer une valeur dans le huitième champ.'
        elif player.round_tg == 3 and values['tg_sendback8']>24:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (24).'
        if player.round_tg == 3 and values['tg_sendback9'] is None:
            return 'Merci de rentrer une valeur dans le neuvième champ.'
        elif player.round_tg == 3 and values['tg_sendback9']>27:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (27).'
        if player.round_tg == 3 and values['tg_sendback10'] is None:
            return 'Merci de rentrer une valeur dans le dixième champ.'
        elif player.round_tg == 3 and values['tg_sendback10']>30:
            return 'Le montant renvoyé ne peut pas être au-delà du montant reçu (30).'

class Game3_4(Page):
    # Belief Elicitation for the first game if it is trust game or pgg.
    form_model = 'player'
    form_fields = ['pgg_beliefintra', 'pgg_beliefinteringroup', 'pgg_beliefinteroutgroup',
                    'tg_belief15', 'tg_belief30']
    @staticmethod
    def is_displayed(player):
        return player.round_tg == 3 or player.round_pgg == 3
    def error_message(player, values):
        if player.round_tg == 3 and values['tg_belief15'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_tg == 3 and values['tg_belief15']>15:
            return 'Le montant renvoyé ne peut pas être plus élevé que le montant reçu.'
        if player.round_tg == 3 and values['tg_belief30'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_tg == 3 and values['tg_belief30']>30:
            return 'Le montant renvoyé ne peut pas être plus élevé que le montant reçu.'        
        if player.round_pgg == 3 and player.condition == "Intra" and values['pgg_beliefintra'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 3 and player.condition == "Intra" and values['pgg_beliefintra']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."
        if player.round_pgg == 3 and player.condition == "Inter" and values['pgg_beliefinteringroup'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 3 and player.condition == "Inter" and values['pgg_beliefinteringroup']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."
        if player.round_pgg == 3 and player.condition == "Inter" and values['pgg_beliefinteroutgroup'] is None:
            return 'Merci de rentrer une valeur.'
        if player.round_pgg == 3 and player.condition == "Inter" and values['pgg_beliefinteroutgroup']>20:
            return "Il n'est pas possible de contribuer plus de 20 ECUs."

class WaitFinish(WaitPage):
        wait_for_all_groups = True
        after_all_players_arrive = 'Alert_Finish'
        title_text = "Vos décisions ont bien été enregistrées"
        body_text = "Merci d'attendre que tous les participants aient pris leurs décisions. Lorsque cela sera fait, cet écran passera automatiquement et un court questionnaire s'affichera sur votre écran."

class Quest1(Page):
    # Questionnaire : demographics
    form_model = 'player'
    form_fields = ['quest_female', 'quest_birthyear','quest_birthplace', 'quest_study']


class Quest2(Page):
    # Questionnaire : trust
    form_model = 'player'
    form_fields = ['quest_trustgovernment', 'quest_trustparliament','quest_trustlocal', 'quest_trustcivilservant',
                   'quest_trustunions', 'quest_trustmedia','quest_trustscientist']

class Quest3(Page):
    # Questionnaire : values
    form_model = 'player'
    form_fields = ['quest_peoplecentrism1', 'quest_peoplecentrism2','quest_antielitism1', 'quest_antielitism2',
                   'quest_manicheism1', 'quest_manicheism2','quest_expertise1','quest_expertise2',
                   'quest_antipolitics1', 'quest_antipolitics2', 'quest_antipopulism1', 'quest_antipopulism2']

class Quest4(Page):
    # Questionnaire : general interest
    form_model = 'player'
    form_fields = ['quest_generalinterest']


class FinalScreen(Page):
    pass

page_sequence = [Initial_Location, Anon,
                 GeneralInstructions,
                 WaitStart,
                 DescriptionINSP,
                 Game1_1, Simulator_TG1, Simulator_PGG1,
                 Simulator_DG1, Game1_2, Game1_3, Game1_4,
                 Game2_1, Simulator_TG2, Simulator_PGG2,
                 Simulator_DG2, Game2_2, Game2_3, Game2_4,
                 Game3_1, Simulator_TG3, Simulator_PGG3,
                 Simulator_DG3,Game3_2,Game3_3, Game3_4,
                 WaitFinish,
                 Quest1,Quest2,Quest3,Quest4,
                 FinalScreen
                 ]
