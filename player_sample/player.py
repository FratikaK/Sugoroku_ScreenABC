class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.money = 10
        self.object = []

    def set_money(self, money):
        self.money = money
        print(self.name + "は" + str(money) + "のお金を受け取った")
        print(self.to_string())

    def add_object(self, object):
        self.object.append(object)
        print(object.name + "の物件を手に入れた")
        print(self.to_string())

    def to_string(self):
        return "-------------------------------------------\n" + "プレイヤー" + self.name + "が所持しているパラメータ\n" \
                                                                                       "お金 : " + str(self.money) + "\n" \
                                                                                                                   "物件数 : " + str(
            len(self.object)) + "\n" \
                                "所持している物件の名前 : " + str(
            self.object)


class Object:
    def __init__(self, object_name):
        self.name = object_name
