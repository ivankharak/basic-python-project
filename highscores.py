#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_worst(scores):
    return min(scores)


def personal_top_x(scores, n):
    return sorted(scores, reverse=True)[0:n]


def personal_worst_x(scores, n):
    return sorted(scores)[0:n]


if __name__ == "__main__":
    scores = [10, 5, 7, 1, 100, 2, 99]
    print(
        f"All Scores: {scores}\nBest: {personal_best(scores)}\nWorst: {personal_worst(scores)}",
        f"\nTop 3: {personal_top_x(scores, 3)}\nWorst 3: {personal_worst_x(scores, 3)}\nLatest: {latest(scores)}",
    )
