#9Mobile USSD Code
#Defining the call-back functions.
def send_back1():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val = int(input("Select an Option; "))
    if snd_val == 0:
        ussd_ii()
    elif snd_val == 99:
        top_up()
    else:
        send_back1()

def send_back2():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val2 = int(input("Select an Option; "))
    if snd_val2 == 0:
        ussd_i()
    elif snd_val2 == 99:
        my_acct()
    else:
        send_back2()

def roam_back():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val7 = int(input("Select an Option; "))
    if snd_val7 == 0:
        ussd_i()
    elif snd_val7 == 99:
        roam_ing()
    else:
        roam_back()

def rng_back():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val8 = int(input("Select an Option; "))
    if snd_val8 == 0:
        ussd_i()
    elif snd_val8 == 99:
        rbtune()
    else:
        rng_back()

def data_back():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val9 = int(input("Select an Option; "))
    if snd_val9 == 0:
        ussd_i()
    # elif snd_val9 == 99:
        # data() Not yet defined...In progress..
    else:
        data_back()

def send_backnin():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val3 = int(input("Select an Option; "))
    if snd_val3 == 0:
        ussd_i()
    elif snd_val3 == 99:
        nin()
    else:
        send_backnin()

def send_back_busn():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val4 = int(input("Select an Option; "))
    if snd_val4 == 0:
        ussd_i()
    elif snd_val4 == 99:
        busi_ness()
    else:
        send_back_busn()

def prep_back():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val6 = int(input("Select an Option; "))
    if snd_val6 == 0:
        ussd_i()
    elif snd_val6 == 99:
        pre_paid()
    else:
        prep_back()

def mre_back():
    print("Invalid Entry.\n"
          "99.Back\n"
          "0.Main Menu")
    snd_val5 = int(input("Select an Option; "))
    if snd_val5  == 0:
        ussd_i()
    elif snd_val5 == 99:
        mre_back()
    else:
        mre_back()

def my_acct():
    print('''\t\t\t1.Check Balance
             2.Check Data
             3.Credit Transfer
             4.Show Number
             5.Check Package
             6.SIM Validity
             7.BOIC ''')
    myacctinp = int(input("Enter a transaction; "))
    if myacctinp == 1:
        print("Your request is being processed.\n"
              "A confirmation SMS about your Airtime Balance will be sent to you shortly.")
    elif myacctinp == 2:
        print("Your request is being processed.\n"
              "A confirmation SMS about your Data Balance will be sent to you shortly.")
    elif myacctinp == 3:
        print("To transfer credit\n"
              "Enter 1*Pin*Amount*Phone No#\n")
        send_back2()
    elif myacctinp == 4:
        print("Your Mobile Number is +2348092351234.")
    elif myacctinp == 5:
        print("Your request is being processed.\n"
              "Please wait,A confirmation SMS will be sent to you shortly.")
    elif myacctinp == 6:
        print("1.1 Year Extension at #500")
        sim_valid = int(input("Select an option; "))
        if sim_valid == 1:
            print("Your Extended SIM Validity will now be renewed.")
        else:
            send_back2()
    elif myacctinp == 7:
        print("1.Check BOIC Status")
        boic_status = int(input("Select an Option; "))
        if boic_status == 1:
            print("You do not have the bonus of incoming calls feature on your line.\n"
                  "Thank You.")
        else:
            send_back2()

# ####def data():
#     print("1.Buy Data\n"
#           "2.Check Data\n"
#           "3.SmartPak\n"
#           "4.Streaming\n"
#           "5.DataGifting\n"
#           "6.DataTransfer\n"
#           "7.Data Family Plan\n"
#           "8.Opt Out.")
#     data_chc = int(input("Select an Option; "))
#     if data_chc == 1:
#     elif data_chc == 2:
#     elif data_chc == 3:
#     elif data_chc == 4:
#     elif data_chc == 5:
#     elif data_chc == 6:
#         print("9Mobile Transfer\n"
#               "")
#         data = int(input("Enter amount of data you want to transfer; "))
#         if  data > 0 and data <= 16:
#             entry2_iv = input("Please provide your account number; ")
#             if len(entry2_iv) == 10:
#                 print("Enter Data amount; ")
#                 entry7 = int(input("; "))
#                 if entry7 > 0:
#                     print(f"Dear Customer,You have successfully been credited with {entry7}MB.\n"
#                           f"Thank you for choosing 9mobile.")
#                 else:
#                     send_back1()
#             else:
#                 send_back1()
#         else:
#             print("Invalid Account Number.")
#             send_back1()
#
#     elif data_chc == 7:
#     elif data_chc == 8:
#         print("Dear Customer,you've successfully opted-out of your Data Plan.\n"
#               "Thank you for choosing 9Mobile.")
#     else:
#         data_back()
#
#Defining the main functions.
def top_up():
    print("1.Top Up from Bank")
    entry = int(input("Select an Option; "))
    if entry == 1:
        print('''\t\t\t\t Welcome to 9mobile!!
                 Please Choose an Option;
                 1.Buy Airtime
                 2.Buy Data
                 3.Add Bank Account
              ''')
        entry2 = int(input("Select an Option; "))
        if entry2 == 1:
           print('''\t\t\t\t9Mobile Airtime TopUp - TopUp Quicker dial *695*Amount#
                            Please Select your Bank;
                            1.Access
                            2.FCMB
                            3.JAIZ
                            4.UNITY
                            5.HERITAGE
                            6.KEYSTONE
                            7.STERLING
                            8.ZENITH
                            9.FIRSTBANK
                            10.ECOBANK
                            11.UNION
                            12.UBA
                            13.GTBANK
                            14.OPAY
                            15.PALMPAY
                            16.KUDA
                        ''')
           entry2_i = int(input("Enter an option; "))
           if entry2_i > 0 and entry2_i <= 16:
              entry2_ii = input("Please provide your account number; ")
              if len(entry2_ii) == 10:
                 print("Enter an amount; ")
                 entry5 = int(input("; "))
                 if entry5 > 0:
                    print(f"You have been credited with {entry5}.")
                 else:
                      send_back1()
              else:
                   print("Invalid Account Number.")
                   send_back1()
           else:
                send_back1()

        elif entry2 == 2:
             print('''\t\t\t\t9Mobile Data TopUp.
                            Please Select your Bank;
                            1.Access
                            2.FCMB
                            3.JAIZ
                            4.UNITY
                            5.HERITAGE
                            6.KEYSTONE
                            7.STERLING
                            8.ZENITH
                            9.FIRSTBANK
                            10.ECOBANK
                            11.UNION
                            12.UBA
                            13.GTBANK
                            14.OPAY
                            15.PALMPAY
                            16.KUDA
                        ''')
             entry2_iii = int(input("Enter an option; "))
             if entry2_iii > 0 and entry2_iii <= 16:
                entry2_iv = input("Please provide your account number; ")
                if len(entry2_iv) == 10:
                    print("Enter Data amount; ")
                    entry7 = int(input("; "))
                    if entry7 > 0:
                       print(f"Dear Customer,You have successfully been credited with {entry7}MB.\n"
                             f"Thank you for choosing 9mobile.")
                    else:
                         send_back1()
                else:
                     send_back1()
             else:
                  print("Invalid Account Number.")
                  send_back1()
        elif entry2 == 3:
            print('''Please Select your Bank;
                            1.Access
                            2.FCMB
                            3.JAIZ
                            4.UNITY
                            5.HERITAGE
                            6.KEYSTONE
                            7.STERLING
                            8.ZENITH
                            9.FIRSTBANK
                            10.ECOBANK
                            11.UNION
                            12.UBA
                            13.GTBANK
                            14.OPAY
                            15.PALMPAY
                            16.KUDA
                      ''')
            entry3_i = int(input("Select an option; "))
            if entry3_i > 0 and entry3_i <= 16:
                entry3_ii = input("Please provide your account number; ")
                if len(entry3_ii) == 10:
                    print("Account Added Successfully.")
                else:
                    print("Invalid Account Number.")
                    send_back1()
            else:
                 send_back1()
        else:
             send_back1()
    else:
        send_back1()

def roam_ing():
    print('''\t\t\t\t1.Roaming Data Bundles
             2.Free Incoming Calls
             3.Corporate Roaming Bundles
          ''')
    roam_bun = int(input("Select an Option; "))
    if roam_bun == 1:
        print('''\t\t\t\t1.Weekly 200MB @ #500
                 2.Monthly 50MB @ #1000
                 3.Check Countries
              ''')
        roam_data = int(input("Select an Option; "))
        if roam_data == 1:
           print("Your request is being processed.\n"
                 "A confirmation SMS will be sent to you shortly.")
        elif roam_bun == 2:
             print("Your request is being processed.\n"
                   "A confirmation SMS will be sent to you shortly.")
        elif roam_bun == 3:
            print("Hello,you can use your data roaming bundle in UK(Vodafone,Telefonica/O2),\n"
                  "USA(T-Mobile),Ghana(Vodafone),\n"
                  "Text MORE to 6589 to see more countries.")
        else:
             roam_back()
    elif roam_bun == 2:
        print("1.Check Eligibility\n"
              "2.Check Countries and Networks")
        roam_calls = int(input("Select an Option; "))
        if roam_calls == 1:
            print("Your request is being processed.\n"
                  "Please wait for a confirmation SMS.\n"
                  "Thank You.")
        elif roam_calls == 2:
            print("Your request is being processed.\n"
                  "Please wait for a confirmation SMS.\n"
                  "Thank You.")
    elif roam_bun == 3:
        print("1.Buy Bundle\n"
              "2.Check Eligible Destinations")
        corp_roam = int(input("Select an Option; "))
        if corp_roam == 1:
            print('''\t\t\t\t1.Social Corporate Bundle
                     2.Basic Corporate Bundle
                     3.Premium Corporate Bundle
                     4.Executive Corporate Bundle
                  ''')
            corp_bund = int(input("Select an Option; "))
            if corp_bund == 1:
               print("1OOMB and 20 minutes talk time at @ 10000 Valid for 15 days.")
               corp_bund_1 = int(input("Select an Option; "))
               if corp_bund_1 == 1:
                   print("Your request is being processed.\n"
                         "Please wait for a confirmation SMS.\n"
                         "Thank You.")
               else:
                   roam_back()
            elif corp_bund == 2:
                 print("300MB and 30 minutes talk time at @ 15000 Valid for 20 days.")
                 corp_bund_2 = int(input("Select an Option; "))
                 if corp_bund_2 == 1:
                     print("Your request is being processed.\n"
                           "Please wait for a confirmation SMS.\n"
                           "Thank You.")
                 else:
                     roam_back()
            elif corp_bund == 3:
                print("500MB and 50 minutes talk time at @ 20000 Valid for 30 days.")
                corp_bund_3 = int(input("Select an Option; "))
                if corp_bund_3 == 1:
                    print("Your request is being processed.\n"
                          "Please wait for a confirmation SMS.\n"
                          "Thank You.")
                else:
                    roam_back()
            elif corp_bund == 4:
                print("1GB and 100 minutes talk time at @ 36000 Valid for 30 days.")
                corp_bund_4 = int(input("Select an Option; "))
                if corp_bund_4 == 1:
                    print("Your request is being processed.\n"
                          "Please wait for a confirmation SMS.\n"
                          "Thank You.")
                else:
                    roam_back()
            else:
                roam_back()

        elif corp_roam == 2:
            print("Hello,you can use your corporate roaming bundle in UK(Vodafone,Telefonica/O2),\n"
                  "USA(T-Mobile),Ghana(Vodafone),UAE(Etisalat),Cameroon(Orange),Japan(Soft Bank),\n"
                  "Text MORE to 6589 to see more countries.")
        else:
            roam_back()
    else:
        roam_back()

def ussd_i():
    ussd = input("Enter USSD Code; ")
    if ussd == "*200#":
        ussd_ii()
    else:
        print("Invalid USSD Code.")
        ussd_i()

def nin():
    print("1.Verify your linked vNIN\n"
          "2.Enter your 16 Digit vNIN\n"
          "3.NIN Registration Centres")
    nin_check = int(input("Select an Option; "))
    if nin_check == 1:
        print("Your request is being processed.\n"
              "A confirmation SMS will be sent to you shortly.")
    elif nin_check == 2:
        nin_val = input("Please Enter your 16 Digit vNIN; ")
        if len(nin_val) == 16:
            print("Thank you for submitting your NIN\n"
                  "Once verified,you'll recieve a confirmation SMS.")
        else:
            send_backnin()
    elif nin_check == 3:
        print("Your request is being processed.\n"
              "A confirmation SMS will be sent to you shortly.")
    else:
        send_backnin()

def rbtune():
    print("Welcome to More Tunes,\n"
          "Select an Option; \n"
          "1.Rora by Reekado Banks\n"
          "2.Hot Tunes\n"
          "3.New Tunes\n"
          "4.More Ring Back Tunes Genre\n"
          "5.Search Tunes\n"
          "6.Subscribe RBT")
    rb_rq = int(input("; "))
    if rb_rq == 1:
        print("Tone Name : Rora by REEKADO BANKS\n"
              "1.Download\n"
              "2.Tariff Price")
        rora = int(input("Select an Option; "))
        if rora == 1:
            print("Dear Customer,you've selected 'Rora' as your Ring Back Tune.\n"
                  "Thank you for choosing 9Mobile.")
        elif rora == 2:
            print("Download Price = #50.00\n"
                      "Gift Price = #50.00\n"
                     "Renew Price = #50.00")
        else:
            rng_back()
    elif rb_rq == 2:
        print("1.Nobody Fine Pass You by T.Classic\n"
              "2.Jowa Bayi by Dami Bliz")
        nbd_rg = int(input("Select an Option"))
        if nbd_rg == 1:
            print("Tone Name : Nobody Fine Pass You\n"
                  "1.Download\n"
                  "2.Tariff Price")
            fine_t = int(input("Select an Option; "))
            if fine_t == 1:
               print("Dear Customer,you've selected 'Nobody Fine Pass You' as your Ring Back Tune.\n"
                      "Thank you for choosing 9Mobile.")
            elif fine_t == 2:
                print("Download Price = #50.00\n"
                      "Gift Price = #50.00\n"
                      "Renew Price = #50.00")
            else:
                rng_back()
        elif nbd_rg == 2:
                print("Tone Name : Jowa Bayi\n"
                      "1.Download\n"
                      "2.Tariff Price")
                jowa_b = int("Select an Option; ")
                if jowa_b == 1:
                    print("Dear Customer,you've selected 'Jowa Bayi' as your Ring Back Tune.\n"
                          "Thank you for choosing 9Mobile.")
                elif jowa_b == 2:
                    print("Download Price = #50.00\n"
                          "Gift Price = #50.00\n"
                          "Renew Price = #50.00")
                else:
                    rng_back()
        else:
            rng_back()
    elif rb_rq == 3:
         print("1.Trobul by Wurld and Sarz\n"
               "2.TIFF by Demmie Vee\n"
               "3.Don't Call Me Back by Joeboy")
         trb_wrld = int(input("Select an Option; "))
         if trb_wrld == 1:
            print("Tone Name : Trobul by Sarz and Wurld\n"
                          "1.Download\n"
                          "2.Tariff Price")
            t_sarz = int(input("Select an Option; "))
            if t_sarz == 1:
               print("Dear Customer,you've selected 'Trobul' as your Ring Back Tune.\n"
                          "Thank you for choosing 9Mobile.")
            elif t_sarz == 2:
                 print("Download Price = #50.00\n"
                          "Gift Price = #50.00\n"
                          "Renew Price = #50.00")
            else:
                 rng_back()
         elif trb_wrld == 2:
              print("Tone Name : TIFF by Demmie Vee\n"
                          "1.Download\n"
                          "2.Tariff Price")
              tiff = int(input("Select an Option; "))
              if tiff == 1:
                 print("Dear Customer,you've selected 'TIFF' as your Ring Back Tune.\n"
                          "Thank you for choosing 9Mobile.")
              elif tiff == 2:
                   print("Download Price = #50.00\n"
                          "Gift Price = #50.00\n"
                          "Renew Price = #50.00")
              else:
                    rng_back()
         elif trb_wrld == 3:
              if trb_wrld == 1:
                 print("Tone Name : Don't Call Me Back by Joeboy\n"
                          "1.Download\n"
                          "2.Tariff Price")
                 dcmb = int(input("Select an Option; "))
                 if dcmb == 1:
                    print("Dear Customer,you've selected 'Don't Call Me Back' as your Ring Back Tune.\n"
                          "Thank you for choosing 9Mobile.")
                 elif dcmb == 2:
                      print("Download Price = #50.00\n"
                          "Gift Price = #50.00\n"
                          "Renew Price = #50.00")
                 else:
                      rng_back()
         else:
              rng_back()

    elif rb_rq == 4:
         print("Dear Customer,you can visit our official site at https://9mobile.cares to Search for More Ring Back Tunes Genre.\n"
               "Thank you for choosing 9Mobile.")
    elif rb_rq == 5:
         print("Dear Customer,you can visit our official site at https://9mobile.cares to Search for More Ring Back Tunes.\n"
                    "Thank you for choosing 9Mobile.")
    elif rb_rq == 6:
        print("Dear Customer,you've successfully been subscribed to the Ring Back Tune Service.")
    else:
        rng_back()

def busi_ness():
    print('''\t\t\t1.MoreBusiness Package
             2.MoreBusiness ComboPak
             3.MoreBusiness 2.0
             4.More Business
             5.SME Share Data
          ''')
    busi_input = int(input("Select an Option; "))
    if busi_input == 1:
        print("1.Migrate to MoreBusiness Package")
        mor_1 = int(input("Select an Option; "))
        if mor_1 == 1:
           print("Your request is being processed.\n"
                  "Please wait,A confirmation SMS will be sent to you shortly.")
        else:
            send_back_busn()
    elif busi_input == 2:
         print("1.Migrate to MoreBusiness ComboPak")
         mor_2 = int(input("Select an Option; "))
         if mor_2 == 1:
            print("Your request is being processed.\n"
                  "Please wait,A confirmation SMS will be sent to you shortly.")
         else:
             send_back_busn()
    elif busi_input == 3:
        print("1.Migrate to MoreBusiness 2.0")
        mor_3 = int(input("Select an Option; "))
        if mor_3 == 1:
           print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        else:
            send_back_busn()
    elif busi_input == 4:
        print("1.Migrate to More Business")
        mor_4 = int(input("Select an Option; "))
        if mor_4 == 1:
           print("Your request is being processed.\n"
                 "Please wait,A confirmation SMS will be sent to you shortly.")
        else:
             send_back_busn()
    elif busi_input == 5:
        print('''\t\t\t\t\t1.Buy SME share data
                 2.Allocate Data Quota
                 3.Recievers List
                 4.Data Balance
                 5.Delete Reciever
                 6.Optout
              ''')
        sme_check = int(input("Select a transaction; "))
        if sme_check == 1:
            print("Your request is being processed\n"
                "Please wait,A confirmation SMS will be sent to you shortly.")
        elif sme_check == 2:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif sme_check == 3:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif sme_check == 4:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif sme_check == 5:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif sme_check == 6:
              print("You have successfuly Opted out of your MoreBusiness plan.\n"
                    "A Confirmation SMS will be sent to you shortly.")
        else:
            send_back_busn()
    else:
        send_back_busn()

def more_credit():
    print("1.More Credit\n"
          "2.Borrow + Save")
    mre_1 = int(input("Select an Option; "))
    if mre_1 == 1:
        print("1.Borrow Airtime"
              "2.Borrow Data")
        brw_mre = int(input("Select an Option; "))
        if brw_mre == 1:
            print('''\t\t\t1.Choose Loan Amount
                     2.Check Eligibity
                     3.Check Debt Status
                     4.Enable Loans
                     5.Disable Loans
                  ''')
            elg_brw = int(input("Select an Option; "))
            if elg_brw == 1:
                print("1.Get #50\n"
                      "2.Get #100\n"
                      "3.Get #200\n"
                      "4.Get #500\n"
                      "5.Get #1000\n"
                      "6.Get #1500\n"
                      "7.Get #2000")
                get_brw = int(input("Select an Option; "))
                if get_brw == 1:
                    print("Your request is being processed.\n"
                          "Thank you for choosing 9mobile.")
                elif get_brw == 2:
                     print("Your request is being processed.\n"
                           "Thank you for choosing 9mobile.")
                elif get_brw == 3:
                     print("Your request is being processed.\n"
                           "Thank you for choosing 9mobile.")
                elif get_brw == 4:
                     print("Your request is being processed.\n"
                            "Thank you for choosing 9mobile.")
                elif get_brw == 5:
                      print("Your request is being processed.\n"
                            "Thank you for choosing 9mobile.")
                elif get_brw == 6:
                    print("Your request is being processed.\n"
                          "Thank you for choosing 9mobile.")
                elif get_brw == 7:
                     print('''Your request is being processed.\n
                              Thank you for choosing 9mobile.
                           ''')
                else:
                    mre_back()

            elif elg_brw == 2:
                 print("1.Get 100MB Valid for 7days\n"
                        "2.Get 250MB valid for 7days\n"
                        "3.Get 50MB valid for 7days\n"
                        "4.Get 500MB Valid 14days\n"
                        "5.Get 1GB Valid 30 days\n"
                        "6.Get 1.5GB Valid 30days\n"
                        "7.Get 2GB Valid 30days.")
                 get_brw_data = int(input("Select an Option; "))
                 if get_brw_data == 1:
                    print('''Your request is being processed.
                            Thank you for choosing 9mobile.
                          ''')
                 elif get_brw_data == 2:
                      print('''Your request is being processed.\n"
                            "Thank you for choosing 9mobile."
                            ''')
                 elif get_brw_data == 3:
                      print('''Your request is being processed.\n"
                               "Thank you for choosing 9mobile."
                           ''')
                 elif get_brw_data == 4:
                      print('''Your request is being processed.\n"
                            "Thank you for choosing 9mobile.
                            ''')
                 elif get_brw_data == 5:
                      print('''Your request is being processed.\n"
                             "Thank you for choosing 9mobile."
                           ''')
                 elif get_brw_data == 6:
                      print('''Your request is being processed.\n"
                              "Thank you for choosing 9mobile."
                           ''')
                 elif get_brw_data == 7:
                      print("Your request is being processed.\n"
                           "Thank you for choosing 9mobile."
                          )
                 else:
                     mre_back()
            else:
                 mre_back()
        elif brw_mre == 2:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif brw_mre == 3:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif brw_mre == 4:
             print("Your request is being processed.\n"
                   "Please wait,A confirmation SMS will be sent to you shortly.")
        elif brw_mre == 5:
             print("Your request is being processed.\n"
                    "Please wait,A confirmation SMS will be sent to you shortly.")
        else:
            mre_back()
    elif mre_1 == 2:
        print("1.Loan + Save\n"
              "2.Help")
        loan = int(input("Select an Option; "))
        if loan == 1:
            print("We currently do not have a loan offer for you,please try again in 30 Days.\n"
                  "Thank you.")
        elif loan == 2:
            print("Text HELP to 561")
    else:
        mre_back()

def pre_paid():
    print("1.More Cliq"
          "2.More Flex Complex"
          "3.Moreflex Plus"
          "4.9 Talk"
          "5.9KonFam")
    pre_check = int(input("Select an Option; "))
    if pre_check == 1:
       print("1.Migrate to More Cliq")
       mre_clq = int(input("Select a transaction; "))
       if mre_clq == 1:
           print("You have successfully migrated to MoreCliq.")
       else:
           pre_paid()
    elif pre_check == 2:
         print("1.Migrate to More Flex Complex.")
         mre_flx = int(input("Select a transaction; "))
         if mre_flx == 1:
            print("You have successfully migrated to More Flex Complex.")
         else:
            pre_paid()

    elif pre_check == 3:
          print("1.Migrate to More Flex Plus")
          mre_flp= int(input("Select a transaction; "))
          if mre_flp == 1:
             print("You have successfully migrated to More Flex Plus.")
          else:
              prep_back()
    elif pre_check == 4:
        print("1.Migrate to 9Talk")
        tlk_9 = int(input("Select a transaction; "))
        if tlk_9 == 1:
            print("You have successfully migrated to 9Talk.")
        else:
            prep_back()

    elif pre_check == 5:
         print("1.Migrate to 9KONFAM")
         con_fam = int(input("Select a transaction; "))
         if con_fam == 1:
            print("You have successfully migrated to 9KONFAM.")
         else:
             prep_back()
    else:
           prep_back()
#The menu, this is where the application starts.
#This is the menu the user sees.
def ussd_ii():
        print('''\t\t\t\t 1.Top Up from Bank
                  2.My Account
                  3.Data
                  4.Prepaid
                  5.Business
                  6.Ring Back Tune
                  7.Roaming
                  8.NIN Check
                  9.MoreCredit
               ''')
        entry = int(input("Select an option; "))
        if entry == 1:
            top_up()
        elif entry == 2:
            my_acct()
        elif entry == 4:
            pre_paid()
        elif entry == 5:
            busi_ness()
        elif entry == 6:
            rbtune()
        elif entry == 7:
            roam_ing()
        elif entry == 8:
            nin()
        elif entry == 9:
            more_credit()
        else:
             print("Invalid Entry.")
             ussd_ii()
#Begins here, this runs the entire application.
ussd_i()
