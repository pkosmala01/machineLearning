import gym
import numpy as np


def GreedyPolicy(env, exProb, qTable, currState):
    if np.random.uniform(0, 1) < exProb:
        action = env.action_space.sample()
    else:
        action = np.argmax(qTable[currState, :])
    return action


def learn(env, episodes, iterPerEp, decayRate, discount, lRate, exProb):
    qTable = np.zeros((env.observation_space.n, env.action_space.n))
    episodeRewards = []
    for ep in range(episodes + 1):
        currState = env.reset()
        epEnd = False
        t = 1
        epReward = 0
        while(t < iterPerEp and not epEnd):
            action = GreedyPolicy(env, exProb, qTable, currState)
            nextState, reward, epEnd, info = env.step(action)
            epReward += reward
            qTable[currState, action] = (1 - lRate) * qTable[currState, action] + lRate * reward + lRate * discount * max(qTable[nextState, :])
            currState = nextState
            t += 1
        if ep % 100 == 0:
            exProb *= decayRate
        episodeRewards.append(epReward)
        if ep % 1000 == 0:
            totalReward = np.mean(episodeRewards)
            print(f'Średnia nagroda po {ep} epizodach: {totalReward}')
            episodeRewards = []
    return totalReward


def testDecay():
    env = gym.make("FrozenLake-v1")
    results = []
    for decay in [0.9, 0.8, 0.75]:
        results.append(learn(env, 5000, 100, decay, 0.99, 0.1, 1))
    print(results)


if __name__ == "__main__":
    # testDecay()
    env = gym.make("FrozenLake-v1")
    learn(env, 5000, 100, 0.8, 0.99, 0.1, 1)
