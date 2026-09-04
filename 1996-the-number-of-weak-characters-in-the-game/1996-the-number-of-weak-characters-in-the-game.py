class Solution:
    def numberOfWeakCharacters(self, properties):

        properties.sort(key=lambda x: (x[0], -x[1]))

        maxDefense = 0
        weak = 0

        for attack, defense in reversed(properties):

            if defense < maxDefense:
                weak += 1

            maxDefense = max(maxDefense, defense)

        return weak