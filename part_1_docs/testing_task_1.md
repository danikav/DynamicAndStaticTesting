<!-- ### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.
<!--  -->
```python

class CardGame:


  def check_for_ace(self, card):
    # need double == to check equality
    if card.value = 1:
      return True
      # need a colon after else
    else
      return False
   
# no comma between card1 and card2
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # changed variable name. It is typed as card, but should be card1
    return card
  else:
    return card2
  


def cards_total(self, cards):
  # total needs to be set as an integer variable, e.g. total = 0
  total
  for card in cards:
    total += card.value
    # the return statement should be unindented so it runs after the loop has completed.
    return "You have a total of" + total
  
```