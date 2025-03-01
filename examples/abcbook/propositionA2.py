"""
Proposition A.2.

From "Multi-Winner Voting with Approval Preferences"
by Martin Lackner and Piotr Skowron
https://arxiv.org/abs/2007.01795
"""

from abcvoting import abcrules
from abcvoting.preferences import Profile
from abcvoting import misc
from abcvoting.output import output
from abcvoting.output import DETAILS


output.set_verbosity(DETAILS)

print(misc.header("Proposition A.2", "*"))

###

num_cand = 3
a, b, c = (0, 1, 2)
approval_sets = [{a}] * 2 + [{a, c}] * 3 + [{b, c}] * 3 + [{b}] * 2
cand_names = "abcde"
profile = Profile(num_cand, cand_names=cand_names)
profile.add_voters(approval_sets)

print(misc.header("1st profile:"))
print(profile.str_compact())


print("winning committees for k=1 and k=2:")
for rule_id in ["pav", "cc", "monroe", "minimaxphragmen", "minimaxav"]:
    comm1 = abcrules.compute(rule_id, profile, 1, resolute=True)[0]
    comm2 = abcrules.compute(rule_id, profile, 2, resolute=True)[0]
    print(
        " "
        + abcrules.Rule(rule_id).shortname
        + ": "
        + misc.str_set_of_candidates(comm1, cand_names)
        + " vs "
        + misc.str_set_of_candidates(comm2, cand_names)
    )
    assert not all(cand in comm1 for cand in comm2)

###

num_cand = 4
a, b, c, d = 0, 1, 2, 3
approval_sets = (
    [{a}] * 6 + [{a, c}] * 4 + [{a, b, c}] * 2 + [{a}] * 2 + [{a, d}] * 1 + [{b, d}] * 3
)
cand_names = "abcde"
profile = Profile(num_cand, cand_names=cand_names)
profile.add_voters(approval_sets)

print()
print(misc.header("2nd profile:"))
print(profile.str_compact())

print("winning committees for k=2 and k=3:")
for rule_id in ["greedy-monroe"]:
    comm1 = abcrules.compute(rule_id, profile, 2, resolute=True)[0]
    comm2 = abcrules.compute(rule_id, profile, 3, resolute=True)[0]
    print(
        f" {abcrules.Rule(rule_id).shortname}: "
        f"{misc.str_set_of_candidates(comm1, cand_names)} vs "
        f"{misc.str_set_of_candidates(comm2, cand_names)}"
    )
    assert not all(cand in comm1 for cand in comm2)

###

num_cand = 6
a, b, c, d, e, f = range(num_cand)
approval_sets = [{a, d, e}, {a, c}, {b, e}, {c, d, f}]
cand_names = "abcdef"
profile = Profile(num_cand, cand_names=cand_names)
profile.add_voters(approval_sets)

print()
print(misc.header("3rd profile:"))
print(profile.str_compact())

print("winning committees for k=3 and k=4:")
comm1 = abcrules.compute(
    "equal-shares", profile, 3, resolute=True, algorithm="standard-fractions"
)[0]
comm2 = abcrules.compute(
    "equal-shares", profile, 4, resolute=True, algorithm="standard-fractions"
)[0]
print(
    f" {abcrules.Rule('equal-shares').shortname}: "
    f"{misc.str_set_of_candidates(comm1, cand_names)} vs "
    f"{misc.str_set_of_candidates(comm2, cand_names)}"
)
assert not all(cand in comm1 for cand in comm2)
