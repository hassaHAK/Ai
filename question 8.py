foods=["birynai","Qourma","Nihari","pizza","burger","pasta","bread","Tikka","Seekh Kabab","Paratha"]
for dish in range(len(foods)):
    print(foods[dish])
    if (dish<3):
        print("This is desi food")
    if ((dish>=3) and (dish<6)):
        print("This is Jung food")
    if ((dish>=6) and (dish<9)):
        print("This is B.B.Q")