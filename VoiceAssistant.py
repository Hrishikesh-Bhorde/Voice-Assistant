import webbrowser
import pyttsx3
import datetime
import wikipedia
import pyscreenshot
import time
import smtplib
from translate import Translator


vo=int(input('which voice do you want sir for male voice press 0 for female voice press 1: '))
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[vo].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime("%I:%M:%S")
    if hour>=0 and hour<12:
        speak("good morning")
        print("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
        print("good afternoon")

    else:
        speak("good evening")
        print("good evening")
        
    speak("the current time is"+time)

    speak("I am Zira . Please tell me how may I help you")
    print("I am zira . Please tell me how may I help you")


if __name__=="__main__" :
    wishme()

the_command = input("how may I help you? ")
def repeath():
                the_command = input("how may I help you? ")
                if the_command == "open google":
                   speak("opening google")
                   webbrowser.open('http://google.co.kr', new=2)
                   repeath()
                elif the_command == "open youtube":
                    speak("opening youtube")
                    webbrowser.open('https://www.youtube.com/', new=2)
                    repeath()
                elif the_command == "open classroom":
                    speak("opening classedge")
                    webbrowser.open('https://classroom.google.com/u/0/h', new=2)
                    repeath()
                elif the_command == "open mail":
                    speak("opening mail")
                    webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox', new=2)
                    repeath()
                elif the_command == "open udemy":
                    speak("opening udemy")
                    webbrowser.open('https://www.udemy.com/cart/success/410771766/', new=2)
                    repeath()
                elif the_command == "open coursera":
                     speak("opening coursera")
                     webbrowser.open('https://www.coursera.org/programs/coursera-response-program-for-cmrk-upa6c', new=2)
                     repeath()
                elif the_command == "open w3 schools":
                    speak("opening w3 schools")
                    webbrowser.open('https://www.w3schools.com/python/default.asp', new=2)
                    repeath()
                elif the_command == "open w3 schools numpy":
                    speak("opening w3 schools numpy")
                    webbrowser.open('https://www.w3schools.com/python/numpy_intro.asp', new=2)
                    repeath()
                elif the_command == "open learning video":
                    speak("opening learning video")
                    webbrowser.open('https://www.youtube.com/watch?v=LHBE6Q9XlzI', new=2)
                    repeath()
                elif the_command == "open neverskip":
                    speak("opening neverskip")
                    webbrowser.open('https://parent.neverskip.com/#/default/dashboard', new=2)
                    repeath()
                elif the_command == "open photos":
                    speak("opening photos")
                    webbrowser.open('https://photos.google.com/u/0/partner/AF1QipMdZvaQZ4NKQMzC_PVt3F0UOmaz?pli=1',)
                    repeath()
                elif the_command == "hi Zira":
                    speak("hi sir")
                    repeath()
                elif the_command == "open games":
                    speak("opening games")
                    webbrowser.open('https://www.agame.com/',)
                    repeath()
                elif the_command == "open ipl":
                    speak("opening ipl")
                    webbrowser.open('https://www.google.com/search?q=ipl&rlz=1C1CHBF_enIN915IN915&oq=ipl&aqs=chrome..69i57j0l6j69i60.2570j1j7&sourceid=chrome&ie=UTF-8',)
                    repeath()
                elif the_command == "sorry to cherry":
                    speak("sorry cherry to cool you down I will show you a pic")
                    webbrowser.open('https://drive.google.com/file/d/1DJayNVeCD8bQeKUJr8M244U3B_pxRw59/view?usp=sharing',)
                    repeath()
                elif the_command == "open uk website":
                    speak("opening uk website")
                    webbrowser.open('https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-c-maintenance-funds',)
                    repeath()
                elif the_command == "open tata classedge":
                    speak ("opening tata classedge")
                    webbrowser.open("https://www.tataclassedgeonline.com/")
                    repeath()
                elif the_command == "open amazon":
                    speak ("opening amazon")
                    webbrowser.open('https://www.amazon.in/')
                    repeath()
                elif the_command == "open flipkart":
                    speak("opening flipkart")
                    webbrowser.open('https://www.flipkart.com/')
                    repeath()
                elif the_command == "search wikipedia":
                    speak("what do you want to search sir")
                    cmd = input("what do you want to search sir ")
                    result = wikipedia.summary(cmd, sentences = 2)
                    print(result)
                    speak(result)
                    repeath()
                elif the_command == "open prime":
                    speak ("opening prime video")
                    webbrowser.open('https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_285art|m_4mEHKPKZc_c442183709740')
                    repeath()
                elif the_command == "open drive":
                    speak("opening google drive")
                    webbrowser.open('drive.google.com/drive/u/1/my-drive')
                    repeath()
                elif the_command == "open project":
                    speak("opening project")
                    webbrowser.open('https://www.education-ecosystem.com/andreybu/RaWGm-how-to-create-a-youtube-clone-in-python-and-django/9b4Kz-youtube_webapp/')
                    repeath()
                elif the_command == "whatsapp":
                    speak ("opening whatsapp ")
                    webbrowser.open('https://web.whatsapp.com/')
                    repeath()
                elif the_command == "teams":
                    speak ("opening teams ")
                    webbrowser.open('https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/conversations/General?threadId=19:639ae767608a4b9d9f70c38441ed83ba@thread.tacv2&ctx=channel')
                    repeath()
                elif the_command == "take screenshot":
                    speak("taking screenshot")
                    time.sleep(2.4)
                    image = pyscreenshot.grab()
                    image.show()
                    speak ("do you want to save the screenshot")
                    ab = input("do you want to save the screenshot: ")
                    if ab == "yes":
                        b = input("name of the screenshot mention .png at the last: ")
                        image.save(b)
                        repeath()
                    elif ab == "no":
                        repeath()
                elif the_command == "search google":
                    speak("What should I search?")
                    vb = input("What should I search?")
                    Search_term = vb.lower()
                    webbrowser.open('https://www.google.com/search?q='+Search_term)
                    repeath()
                elif the_command == "search youtube":
                    speak("What should I search?")
                    b = input("What should I search? ")
                    Searchterm = b.lower()
                    speak("Here we go to Youtube\n")
                    webbrowser.open("https://www.youtube.com/results?search_query="+Searchterm)
                    repeath()
                elif "where is" in the_command:
                    the_command = the_command.replace("where is", "")
                    location = the_command
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.com/maps/place/" + location)
                    repeath()
                elif the_command == "compose email":
                    speak("composing email")
                    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
                    repeath()
                elif the_command == "search rgu mails":
                    speak("searching rgu emails")
                    webbrowser.open("https://mail.google.com/mail/u/1/#search/rgu")
                    repeath()
                elif the_command == "search mail":
                    speak("What should I search?")
                    vt = input("What should I search?")
                    Search = vt.lower()
                    webbrowser.open('https://mail.google.com/mail/u/1/#search/'+Search)
                    repeath()
                elif the_command == "send email":
                    speak("whom do you want to send email")
                    Send_email = input("Sender E-mail id: ")
                    speak("what message do you want to send sir")
                    Mess_age = input("Message: ")
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login("nehabhosale1006@gmail.com", "NehE0506")
                    s.sendmail("nehabhosale1006@gmail.com", Send_email, Mess_age)
                    s.quit()
                    repeath()
                elif the_command == "who is the creater of you":
                    speak("I am created by V Harivansh reddy")
                    print("I am created by V Harivansh reddy")
                    print("You can contact him by E-mail : harivanshreddy21@gmail.com")
                elif the_command == "open time table":
                    speak ("opening your time table")
                    webbrowser.open('https://drive.google.com/file/d/1l2wgApR1G6cancmqjyIO_Wtm41CZENkC/view?usp=sharing')
                    repeath()
                elif the_command == "translate":
                    speak("which language do you want to translate sir")
                    tr = input("which language do you want to translate sir: ")
                    speak("which word do you want to translate sir")
                    wo = input("which word do you want to translate sir: ")
                    translator= Translator(to_lang=tr)
                    translation = translator.translate(wo)
                    print (translation)
                    speak (translation)
                    repeath()
                elif the_command == "open instagram":
                    speak("opening instagram")
                    webbrowser.open("https://www.instagram.com/")
                    repeath()
                elif the_command == "open facebook":
                    speak("opening facebook")
                    webbrowser.open("https://www.facebook.com/")
                    repeath()
                elif the_command == "open bing":
                    speak("opening bing")
                    webbrowser.open("youtube.com")
                    repeath()
                elif the_command == "see earth":
                    speak("I will show you the earth")
                    webbrowser.open("https://www.google.co.in/maps/@-47.818968,50.3171231,22935868m/data=!3m1!1e3?hl=en")
                    repeath()
                elif the_command == "see mercury":
                    speak("I will show you the mercury")
                    webbrowser.open("https://www.google.co.in/maps/space/mercury/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
                    repeath()
                elif the_command == "see venus":
                    speak("I will show you the venus")
                    webbrowser.open("https://www.google.co.in/maps/space/venus/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
                    repeath()
                elif the_command == "see moon":
                    speak("I will show you the moon")
                    webbrowser.open("https://www.google.co.in/maps/space/moon/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
                    repeath()
                elif the_command == "see mars":
                    speak("I will show you the mars")
                    webbrowser.open("https://www.google.co.in/maps/space/mars/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
                    repeath()
                elif the_command == "see space station":
                    speak("I will show you the earth")
                    webbrowser.open("https://www.google.co.in/maps/space/iss/@29.5602853,-95.0853914,2a,75y,260h,90t/data=!3m6!1e1!3m4!1szChzPIAn4RIAAAQvxgbyEg!2e0!7i10000!8i5000?hl=en")
                    repeath()
                elif the_command == "open meet":
                    speak("opening meet")
                    webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
                    repeath()
                elif the_command == "thank you":
                    speak("its my pleasure sir")
                    quit()
                elif the_command == "cl":
                    speak("opening classedge")
                    webbrowser.open("https://live.tataclassedgeonline.com/ilc/#/home")
                    repeath()
                elif the_command == "sg":
                    speak("What should I search?")
                    vb = input("What should I search?")
                    Search_term = vb.lower()
                    webbrowser.open('https://www.google.com/search?q='+Search_term)
                    repeath()
                elif the_command == "flights from hyderabad to london":
                    speak("opening classedge")
                    webbrowser.open("https://www.google.com/travel/flights/booking?tfs=CBwQAhpJagwIAhIIL20vMDljNncSCjIwMjEtMDEtMTVyDAgCEggvbS8wNGpwbCIfCgNIWUQSCjIwMjEtMDEtMTUaA0xIUioCQkEyAzI3NnABggELCP___________wFAAUgBmAEC&tfu=CpQBQ2lkSE1VUlBWa0pITFMwdExTMHRMUzB0ZEdoemN6YzRRVUZCUVVGR1gwVnJNRFJETTFCVFFVRVNCVUpCTWpjMkdnc0k1c2tCRUFBYUEwbE9VamdjUUFCS0JBZ0JFQUZTQWtKQldnSkNRV0lZTWpBeU1TMHdNUzB4TlRwSVdVUTZURWhTT2tKQk1qYzJjT1NRQWc9PQ&hl=en&authuser=0")
                    repeath()
                elif the_command == "hyderabad to london":
                    speak("opening flights from hyderabad to london")
                    webbrowser.open("https://www.google.com/travel/flights/booking?tfs=CBwQAhpJagwIAhIIL20vMDljNncSCjIwMjEtMDEtMTVyDAgCEggvbS8wNGpwbCIfCgNIWUQSCjIwMjEtMDEtMTUaA0xIUioCQkEyAzI3NnABggELCP___________wFAAUgBmAEC&tfu=CpQBQ2lkSE1VUlBWa0pITFMwdExTMHRMUzB0ZEdoemN6YzRRVUZCUVVGR1gwVnJNRFJETTFCVFFVRVNCVUpCTWpjMkdnc0k1c2tCRUFBYUEwbE9VamdjUUFCS0JBZ0JFQUZTQWtKQldnSkNRV0lZTWpBeU1TMHdNUzB4TlRwSVdVUTZURWhTT2tKQk1qYzJjT1NRQWc9PQ&hl=en&authuser=0")
                    repeath()
                elif the_command == "banglore to london":
                    speak("opening flights from banglore to london")
                    webbrowser.open("https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAhIIL20vMDljMTcSCjIwMjEtMDEtMTRyBwgBEgNMSFJwAYIBCwj___________8BQAFIAZgBAg&hl=en&authuser=0")
                    repeath()
                elif the_command == "time":
                    print(time)
                    repeath()
                elif the_command == "open google maps":
                    speak ("opening google maps")
                    webbrowser.open('https://maps.google.co.in/maps?hl=en&tab=rl&authuser=0')
                    repeath()
                elif the_command == "open google classroom":
                    speak ("opening google classroom")
                    webbrowser.open('https://classroom.google.com/?authuser=0')
                    repeath()
                elif the_command == "open google photos":
                    speak ("opening google photos")
                    webbrowser.open('https://classroom.google.com/?authuser=0')
                    repeath()
                elif the_command == "open google shopping":
                    speak ("opening google shopping")
                    webbrowser.open('https://www.google.co.in/shopping?hl=en&source=og&tab=rf&authuser=0')
                    repeath()
                elif the_command == "open google duo":
                    speak ("opening google duo")
                    webbrowser.open('https://duo.google.com/?usp=duo_ald')
                    repeath()
                elif the_command == "open google news":
                    speak ("opening google news")
                    webbrowser.open('https://news.google.com/?tab=rn&authuser=0')
                    repeath()
                elif the_command == "open google meet":
                    speak ("opening google meet")
                    webbrowser.open('https://meet.google.com/?hs=197&pli=1&authuser=0')
                    repeath()
                elif the_command == "open google docs":
                    speak ("opening google docs")
                    webbrowser.open('https://docs.google.com/document/?usp=docs_alc&authuser=0')
                    repeath()
                elif the_command == "open google spreadsheets":
                    speak ("opening google spreadsheets")
                    webbrowser.open('https://docs.google.com/spreadsheets/?usp=sheets_alc&authuser=0')
                    repeath()
                elif the_command == "open google slides":
                    speak ("opening google slides")
                    webbrowser.open('https://docs.google.com/presentation/?usp=slides_alc&authuser=0')
                    repeath()
                elif the_command == "open hangouts":
                    speak ("opening google hangouts")
                    webbrowser.open('https://hangouts.google.com/?authuser=0')
                    repeath()
                elif the_command == "open blogger":
                    speak ("opening google blogger")
                    webbrowser.open('https://www.blogger.com/?tab=rj&authuser=0')
                    repeath()                    
                else:
                    Search_term = the_command.lower()
                    webbrowser.open('https://www.google.com/search?q='+Search_term)
                    speak("these are the results from the web")
                    repeath()
                    
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
if the_command == "open google":
    speak("opening google")
    webbrowser.open('http://google.co.kr', new=2)
    repeath()
elif the_command == "open youtube":
    speak("opening youtube")
    webbrowser.open('https://www.youtube.com/', new=2)
    repeath()
elif the_command == "open classedge":
    speak("opening classedge")
    webbrowser.open('https://live.tataclassedgeonline.com/ilc/#/home', new=2)
    repeath()
elif the_command == "open mail":
    speak("opening mail")
    webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox', new=2)
    repeath()
elif the_command == "open udemy":
    speak("opening udemy")
    webbrowser.open('https://www.udemy.com/cart/success/410771766/', new=2)
    repeath()
elif the_command == "open coursera":
     speak("opening coursera")
     webbrowser.open('https://www.coursera.org/programs/coursera-response-program-for-cmrk-upa6c', new=2)
     repeath()
elif the_command == "open w3 schools":
    speak("opening w3 schools")
    webbrowser.open('https://www.w3schools.com/python/default.asp', new=2)
    repeath()
elif the_command == "open w3 schools numpy":
    speak("opening w3 schools numpy")
    webbrowser.open('https://www.w3schools.com/python/numpy_intro.asp', new=2)
    repeath()
elif the_command == "open learning video":
    speak("opening learning video")
    webbrowser.open('https://www.youtube.com/watch?v=LHBE6Q9XlzI', new=2)
    repeath()
elif the_command == "open neverskip":
    speak("opening neverskip")
    webbrowser.open('https://parent.neverskip.com/#/default/dashboard', new=2)
    repeath()
elif the_command == "open photos":
    speak("opening photos")
    webbrowser.open('https://photos.google.com/u/0/partner/AF1QipMdZvaQZ4NKQMzC_PVt3F0UOmaz?pli=1',)
    repeath()
elif the_command == "hi thunder":
    speak("hi sir")
    repeath()
elif the_command == "open games":
    speak("opening games")
    webbrowser.open('https://www.agame.com/',)
    repeath()
elif the_command == "open ipl":
    speak("opening ipl")
    webbrowser.open('https://www.google.com/search?q=ipl&rlz=1C1CHBF_enIN915IN915&oq=ipl&aqs=chrome..69i57j0l6j69i60.2570j1j7&sourceid=chrome&ie=UTF-8',)
    repeath()
elif the_command == "sorry to cherry":
    speak("sorry cherry to cool you down I will show you a pic")
    webbrowser.open('https://drive.google.com/file/d/1DJayNVeCD8bQeKUJr8M244U3B_pxRw59/view?usp=sharing',)
    repeath()
elif the_command == "open uk website":
    speak("opening uk website")
    webbrowser.open('https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-c-maintenance-funds',)
    repeath()
elif the_command == "open tata classedge":
    speak ("opening tata classedge")
    webbrowser.open("https://www.tataclassedgeonline.com/")
    repeath()
elif the_command == "open amazon":
    speak ("opening amazon")
    webbrowser.open('https://www.amazon.in/')
    repeath()
elif the_command == "open flipkart":
    speak("opening flipkart")
    webbrowser.open('https://www.flipkart.com/')
    repeath()
elif the_command == "search wikipedia":
    speak("what do you want to search sir")
    cmd = input("what do you want to search sir ")
    result = wikipedia.summary(cmd, sentences = 2)
    print(result)
    speak(result)
    repeath()
elif the_command == "open prime":
    speak ("opening prime vedio")
    webbrowser.open('https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_285art|m_4mEHKPKZc_c442183709740')
    repeath()
elif the_command == "open drive":
    speak("opening google drive")
    webbrowser.open('drive.google.com/drive/u/1/my-drive')
    repeath()
elif the_command == "open project":
    speak("opening project")
    webbrowser.open('https://www.education-ecosystem.com/andreybu/RaWGm-how-to-create-a-youtube-clone-in-python-and-django/9b4Kz-youtube_webapp/')
    repeath()
elif the_command == "whatsapp":
    speak ("opening whatsap ")
    webbrowser.open('https://web.whatsapp.com/')
    repeath()
elif the_command == "teams":
    speak ("opening teams ")
    webbrowser.open('https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/conversations/General?threadId=19:639ae767608a4b9d9f70c38441ed83ba@thread.tacv2&ctx=channel')
    repeath()
elif the_command == "take a screenshot":
    speak("taking screenshot")
    time.sleep(2.4)
    image = pyscreenshot.grab()
    image.show()
    speak ("do you want to save the screenshot")
    ab = input("do you want to save the screenshot: ")
    if ab == "yes":
        b = input("name of the screenshot mention .png at the last: ")
        image.save(b)
        repeath()
    elif ab == "no":
        repeath()
elif the_command == "search google":
    speak("What should I search?")
    vb = input("What should I search?")
    Search_term = vb.lower()
    webbrowser.open('https://www.google.com/search?q='+Search_term)
    repeath()
elif the_command == "search youtube":
    speak("What should I search?")
    b = input("What should I search? ")
    Searchterm = b.lower()
    speak("Here we go to Youtube\n")
    webbrowser.open("https://www.youtube.com/results?search_query="+Searchterm)
    repeath()
elif "where is" in the_command:
    the_command = the_command.replace("where is", "")
    location = the_command
    speak("you asked to Locate")
    speak(location)
    webbrowser.open("https://www.google.com/maps/place/" + location)
    repeath()
elif the_command == "compose email":
    speak("composing email")
    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
    repeath()
elif the_command == "search rgu mails":
    speak("searching rgu emails")
    webbrowser.open("https://mail.google.com/mail/u/1/#search/rgu")
    repeath()
elif the_command == "search mail":
    speak("What should I search?")
    vt = input("What should I search?")
    Search = vt.lower()
    webbrowser.open('https://mail.google.com/mail/u/1/#search/'+Search)
    repeath()
elif the_command == "send email":
    speak("whom do you want to send email")
    Send_email = input("Sender E-mail id: ")
    speak("what message do you want to send sir")
    Mess_age = input("Message: ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("harivanshreddy21@gmail.com", "nanamma@123")
    s.sendmail("harivanshreddy21@gmail.com", Send_email, Mess_age)
    s.quit()
    repeath()
elif the_command == "quit":
    speak("thank you sir")
    quit()
elif the_command == "who created you":
    speak("I am created by V Harivansh reddy")
    print("I am created by V Harivansh reddy")
    print("You can contact him by E-mail : harivanshreddy21@gmail.com")
    repeath()
elif the_command == "open time table":
    speak ("opening your time table")
    webbrowser.open('https://drive.google.com/file/d/1l2wgApR1G6cancmqjyIO_Wtm41CZENkC/view?usp=sharing')
    repeath()
elif the_command == "translate":
    tr = input("which language do you want to translate sir: ")
    speak("which language do you want to translate sir")
    wo = input("which word do you want to translate sir: ")
    speak("which word do you want to translate sir")
    translator= Translator(to_lang=tr)
    translation = translator.translate(wo)
    print (translation)
    speak (translation)
    repeath()
elif the_command == "open instagram":
    speak("opening instagram")
    webbrowser.open("https://www.instagram.com/")
    repeath()
elif the_command == "open facebook":
    speak("opening facebook")
    webbrowser.open("https://www.facebook.com/")
    repeath()
elif the_command == "open bing":
    speak("opening bing")
    webbrowser.open("youtube.com")
    repeath()
elif the_command == "see earth":
    speak("I will show you the earth")
    webbrowser.open("https://www.google.co.in/maps/@-51.6273648,153.285256,6429359m/data=!3m1!1e3?hl=en")
    repeath()
elif the_command == "see mercury":
    speak("I will show you the mercury")
    webbrowser.open("https://www.google.co.in/maps/space/mercury/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
    repeath()
elif the_command == "see venus":
    speak("I will show you the venus")
    webbrowser.open("https://www.google.co.in/maps/space/venus/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
    repeath()
elif the_command == "see moon":
    speak("I will show you the moon")
    webbrowser.open("https://www.google.co.in/maps/space/moon/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
    repeath()
elif the_command == "see mars":
    speak("I will show you the mars")
    webbrowser.open("https://www.google.co.in/maps/space/mars/@-47.818968,50.3171231,22671583m/data=!3m1!1e3?hl=en")
    repeath()
elif the_command == "see space station":
    speak("I will show you the earth")
    webbrowser.open("https://www.google.co.in/maps/space/iss/@29.5602853,-95.0853914,2a,75y,260h,90t/data=!3m6!1e1!3m4!1szChzPIAn4RIAAAQvxgbyEg!2e0!7i10000!8i5000?hl=en")
    repeath()
elif the_command == "open meet":
    speak("opening meet")
    webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
    repeath()
elif the_command == "thank you":
    speak("its my pleasure sir")
    quit()
elif the_command == "cl":
    speak("opening classedge")
    webbrowser.open("https://live.tataclassedgeonline.com/ilc/#/home")
    repeath()
elif the_command == "sg":
    speak("What should I search?")
    vb = input("What should I search?")
    Search_term = vb.lower()
    webbrowser.open('https://www.google.com/search?q='+Search_term)
    repeath()
elif the_command == "flights from hyderabad to london":
    speak("opening classedge")
    webbrowser.open("https://www.google.com/travel/flights/booking?tfs=CBwQAhpJagwIAhIIL20vMDljNncSCjIwMjEtMDEtMTVyDAgCEggvbS8wNGpwbCIfCgNIWUQSCjIwMjEtMDEtMTUaA0xIUioCQkEyAzI3NnABggELCP___________wFAAUgBmAEC&tfu=CpQBQ2lkSE1VUlBWa0pITFMwdExTMHRMUzB0ZEdoemN6YzRRVUZCUVVGR1gwVnJNRFJETTFCVFFVRVNCVUpCTWpjMkdnc0k1c2tCRUFBYUEwbE9VamdjUUFCS0JBZ0JFQUZTQWtKQldnSkNRV0lZTWpBeU1TMHdNUzB4TlRwSVdVUTZURWhTT2tKQk1qYzJjT1NRQWc9PQ&hl=en&authuser=0")
    repeath()
elif the_command == "hyderabad to london":
    speak("opening flights from hyderabad to london")
    webbrowser.open("https://www.google.com/travel/flights/booking?tfs=CBwQAhpJagwIAhIIL20vMDljNncSCjIwMjEtMDEtMTVyDAgCEggvbS8wNGpwbCIfCgNIWUQSCjIwMjEtMDEtMTUaA0xIUioCQkEyAzI3NnABggELCP___________wFAAUgBmAEC&tfu=CpQBQ2lkSE1VUlBWa0pITFMwdExTMHRMUzB0ZEdoemN6YzRRVUZCUVVGR1gwVnJNRFJETTFCVFFVRVNCVUpCTWpjMkdnc0k1c2tCRUFBYUEwbE9VamdjUUFCS0JBZ0JFQUZTQWtKQldnSkNRV0lZTWpBeU1TMHdNUzB4TlRwSVdVUTZURWhTT2tKQk1qYzJjT1NRQWc9PQ&hl=en&authuser=0")
    repeath()
elif the_command == "banglore to london":
    speak("opening flights from banglore to london")
    webbrowser.open("https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAhIIL20vMDljMTcSCjIwMjEtMDEtMTRyBwgBEgNMSFJwAYIBCwj___________8BQAFIAZgBAg&hl=en&authuser=0")
    repeath()
elif the_command == "time":
    print(time)
    repeath()
elif the_command == "open google maps":
    speak ("opening google maps")
    webbrowser.open('https://maps.google.co.in/maps?hl=en&tab=rl&authuser=0')
    repeath()
elif the_command == "open google classroom":
    speak ("opening google classroom")
    webbrowser.open('https://classroom.google.com/?authuser=0')
    repeath()
elif the_command == "open google photos":
    speak ("opening google photos")
    webbrowser.open('https://classroom.google.com/?authuser=0')
    repeath()
elif the_command == "open google shopping":
    speak ("opening google shopping")
    webbrowser.open('https://www.google.co.in/shopping?hl=en&source=og&tab=rf&authuser=0')
    repeath()
elif the_command == "open google duo":
    speak ("opening google duo")
    webbrowser.open('https://duo.google.com/?usp=duo_ald')
    repeath()
elif the_command == "open google news":
    speak ("opening google news")
    webbrowser.open('https://news.google.com/?tab=rn&authuser=0')
    repeath()
elif the_command == "open google meet":
    speak ("opening google meet")
    webbrowser.open('https://meet.google.com/?hs=197&pli=1&authuser=0')
    repeath()
elif the_command == "open google docs":
    speak ("opening google docs")
    webbrowser.open('https://docs.google.com/document/?usp=docs_alc&authuser=0')
    repeath()
elif the_command == "open google spreadsheets":
    speak ("opening google spreadsheets")
    webbrowser.open('https://docs.google.com/spreadsheets/?usp=sheets_alc&authuser=0')
    repeath()
elif the_command == "open google slides":
    speak ("opening google slides")
    webbrowser.open('https://docs.google.com/presentation/?usp=slides_alc&authuser=0')
    repeath()
elif the_command == "open hangouts":
    speak ("opening google hangouts")
    webbrowser.open('https://hangouts.google.com/?authuser=0')
    repeath()
elif the_command == "open blogger":
    speak ("opening google blogger")
    webbrowser.open('https://www.blogger.com/?tab=rj&authuser=0')
    repeath()
else:
    Search_term = the_command.lower()
    webbrowser.open('https://www.google.com/search?q='+Search_term)
    speak("these are the results from the web")
    repeath()
  