from ric_core import replay_history

x0 = 10
transitions = [+3, -2, +4, -1, +2]

h1, c1 = replay_history(x0, transitions)
h2, c2 = replay_history(x0, transitions)

print("Replay Identity Capsule Demo")
print("----------------------------")
print()
print("Initial state :", x0)
print("Transitions   :", transitions)
print()
print("History run A :", h1)
print("History run B :", h2)
print()
print("Replay identity :", c1 == c2)
print("Capsule         :", c1[:16] + "...")
print()
print("RIC execution complete.")