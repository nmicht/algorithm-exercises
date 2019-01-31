/*
X of a Kind in a deck of cards
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
 */
#define MAXINT 10000

bool hasGroupsSizeX(int* deck, int deckSize)
{
  int count[MAXINT] = {0};
  int smallest = MAXINT;
  int maxCountIndex = 0;

  for (int i=0; i < deckSize; i++) {
    count[deck[i]]++;
    if (deck[i] > maxCountIndex)
      maxCountIndex = deck[i];
  }

  for (int i=0; i <= maxCountIndex; i++) {
    if (count[i] != 0 && count[i] < smallest)
      smallest = count[i];
  }

  for (int d=2; d <= smallest; d++) {
    bool canDivide = true;
    for (int i=0; i < maxCountIndex; i++) {
      if (count[i] && count[i] % d) {
        canDivide = false;
        break;
      }
    }
    if (canDivide)
      return true;
  }
  return false;
}
