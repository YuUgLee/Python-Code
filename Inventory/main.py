import InventoryTEST

def main():

    while True:
        InventoryTEST.refreshDataFrame()
        user = int(input("--MENU--\nWhat would you like to do?\n1. Find Product\n2. Add Product\n3. Delete Product\n4. Change Name\n5. Change Location\n6. Change Part Number\n7. Change Quantity\n8. Change Decryption\n9. Change Note\n"))
        while True:
            if user == 1:
                data = int(input("Please enter what Part Number you would like to find:\n"))
                if InventoryTEST.findPartNumber(data) == False:
                    print("Part Number could not be found.")
                    continue
                else:
                    print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(data)])
                    input("Press ENTER to continue:\n")
                break
            if user == 2:
                InventoryTEST.addProduct()
                break
            if user == 3:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.deleteProduct(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
            if user == 4:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.changeName(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
            if user == 5:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.changeLocation(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
            if user == 6:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.changePartNumber(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
            if user == 7:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.changeQuantity(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
            if user == 8:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.changeDecryption(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
            if user == 9:
                num = int(input("Enter Part number:"))
                if InventoryTEST.findPartNumber(num) == False:
                    continue
                print(InventoryTEST.df.loc[InventoryTEST.findPartNumber(num)])
                user = input("Is this the correct product?")
                if user.capitalize() == "Y":
                    InventoryTEST.changeNote(num)
                    break
                else:
                    continue
                InventoryTEST.refreshDataFrame()
    # InventoryTEST.refreshDataFrame()
    # print(InventoryTEST.df.shape[0])


main()
# def main():
#     while True:
#         Inventory.refreshDataFrame()
#         user = int(input("--MENU--\nWhat would you like to do?\n1. Find Product\n2. Change Name\n3. Change Location\n4. Change Part Number\n5. Change Quantity\n6. Change Decryption\n7. Change Note\n"))
#         while True:
#             if user == 1:
#                 data = int(input("Please enter what Part Number you would like to find:\n"))
#                 Inventory.findPartNumber(data)
#                 input("Press ENTER to continue:\n")
#                 break
#             row = int(input("Please select which row you would like to change:\n"))
#             print(Inventory.df.loc[[row]])
#             verify = input("Is this the correct row? (Y/N)")
#
#             if verify.capitalize() == "Y":
#
#                 if user == 2:
#                     data = input("Please enter what Name you would like to change to:\n")
#                     Inventory.changeName(row,data)
#                     break
#                 if user == 3:
#                     data = input("Please enter what Location you would like to change to:\n")
#                     Inventory.changeLocation(row,data)
#                     break
#                 if user == 4:
#                     data = int(input("Please enter what Part Number you would like to change to:\n"))
#                     Inventory.changePartNumber(row,data)
#                     break
#                 if user == 5:
#                     data = int(input("Please enter what Quantity you would like to change to:\n"))
#                     Inventory.changeQuantity(row,data)
#                     break
#                 if user == 6:
#                     data = input("Please enter what Decryption you would like to change to:\n")
#                     Inventory.changeDecryption(row,data)
#                     break
#                 if user == 7:
#                     data = input("Please enter what Note you would like to change to:\n")
#                     Inventory.changeNote(row,data)
#                     break
#
#             elif verify.capitalize() == "N":
#                 continue
# main()

