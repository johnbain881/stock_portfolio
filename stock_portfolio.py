stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 )
]

purchase_portfolio = {}

for purchase in purchases:
  purchase_portfolio[purchase[0]] = 0

for key in purchase_portfolio:
  print(f"------ {key} ------")
  tally = 0
  for purchase in purchases:
    if purchase[0] == key:
      tally = tally + purchase[1] * purchase[3]
      print(f"{purchase[1]} shares at {purchase[3]} dollars each on {purchase[2]}")
  print(f"\nTotal value of stock in portfolio ${tally}\n")