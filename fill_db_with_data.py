import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from polls.models import Choice, Question 
from django.utils import timezone

q = Question(question_text="Welcher Urlaubstyp bist du?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Städtereise", votes=0)
q.choice_set.create(choice_text="Strandurlaub", votes=0)
q.choice_set.create(choice_text="Natur pur", votes=0)
q.choice_set.create(choice_text="Partyurlaub", votes=0)
q.choice_set.create(choice_text="Aktivurlaub", votes=0)
q.save()

q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Not much!", votes=0)
q.choice_set.create(choice_text="The sky!", votes=0)
q.choice_set.create(choice_text="Beach!", votes=0)
q.choice_set.create(choice_text="Party!", votes=0)
q.choice_set.create(choice_text="I'm hungry!", votes=0)
q.save()

q = Question(question_text="Was ist deine Liblingsfarbe?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Weiß", votes=0)
q.choice_set.create(choice_text="Schwarz", votes=0)
q.choice_set.create(choice_text="Silber", votes=0)
q.choice_set.create(choice_text="Rot", votes=0)
q.choice_set.create(choice_text="Orange", votes=0)
q.choice_set.create(choice_text="Gelb", votes=0)
q.choice_set.create(choice_text="Grün", votes=0)
q.choice_set.create(choice_text="Blau", votes=0)
q.choice_set.create(choice_text="Violett", votes=0)

q = Question(question_text="Welches Haustier hast du oder möchtest du haben?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Hund", votes=0)
q.choice_set.create(choice_text="Katze", votes=0)
q.choice_set.create(choice_text="Schaf", votes=0)
q.choice_set.create(choice_text="Kuh", votes=0)
q.choice_set.create(choice_text="Schwein", votes=0)
q.choice_set.create(choice_text="Tiger", votes=0)
q.choice_set.create(choice_text="Elch", votes=0)
q.choice_set.create(choice_text="Elefant", votes=0)

q = Question(question_text="Was ist deine Wohlfühltemperatur im Schlafzimmer?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Je kälter desto besser. Auch wenn es draußen friert ist das Fenster offen.", votes=0)
q.choice_set.create(choice_text="Etwas zwichen 16°C und 18°C.", votes=0)
q.choice_set.create(choice_text="Mindestens 19°C aber nicht mehr als 20°", votes=0)
q.choice_set.create(choice_text="Ich bin verwarmt und brauche am mehr.", votes=0)

q = Question(question_text="Welche Küche magst du am liebsten?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Orientalisch", votes=0)
q.choice_set.create(choice_text="Italienisch", votes=0)
q.choice_set.create(choice_text="Chinesisch", votes=0)
q.choice_set.create(choice_text="Thailändisch", votes=0)
q.choice_set.create(choice_text="Klassisch mitteleuropäisch", votes=0)
q.choice_set.create(choice_text="Amerikanisch", votes=0)

q = Question(question_text="Was snackst du?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Schokolade, Eis, hauptsache süß", votes=0)
q.choice_set.create(choice_text="Banane, Weintrauben oder sonstige Früchte", votes=0)
q.choice_set.create(choice_text="Chips, Salzstangen, am liebsten pikant und salzig", votes=0)
q.choice_set.create(choice_text="Snacks sind doch ungesund", votes=0)

q = Question(question_text="Wie kommst du zur Arbeit?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text="Zu Fuß", votes=0)
q.choice_set.create(choice_text="Mit dem Fahrrad", votes=0)
q.choice_set.create(choice_text="Mit dem Auto", votes=0)
q.choice_set.create(choice_text="ÖPNV", votes=0)
q.choice_set.create(choice_text="Am liebsten beamen", votes=0)

# Query first questions and all choices to vote
all_questions = Question.objects.all()

print(f"there are {len(all_questions)} question objects\n", Question.objects.all())

q = Question.objects.get(pk=1)

print("question")
print(f"id:       {q.id}")
print(f"text:     {q.question_text}")
print(f"pub_date: {q.pub_date}")

n_choices = q.choice_set.count()
print(f"number of choices: {n_choices}")
for i in range(n_choices):
  c=q.choice_set.all()[i]
  print("  > ", c, c.id, c.question_id, c.votes)

# get query sets
q_qset = Question.objects.filter(question_text__startswith="Was")
print(q_qset)
c_qset = Choice.objects.filter(question__pk=2)
print(c_qset.get(id=7))