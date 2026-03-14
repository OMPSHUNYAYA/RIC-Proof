import hashlib

def replay_history(x0, transitions):
    x = x0
    history = [x0]
    for d in transitions:
        x += d
        history.append(x)
    payload = "->".join(map(str, history))
    capsule = hashlib.sha256(payload.encode()).hexdigest()
    return history, capsule