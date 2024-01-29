
class monkey:
    species = ''
    sex = ''
    color = ''
    weight = 0.0

    def make_fire(self, tool):
        if tool == '石头':
            print("猴子用" + tool + "造火")
        elif tool == '木棍':
            print("猴子用" + tool + "造火")

    def learn(self, things):
        print("猴子学", things)


sunwukong = monkey()
sunwukong.learn('游泳')
