class MemberCounter:
    member = 1;
    def init(self):
        MemberCounter.member += 1

m1 = MemberCounter()
m1.init()
print MemberCounter.member
m2 = MemberCounter()
m2.init()
print MemberCounter.member

print m1.__class__