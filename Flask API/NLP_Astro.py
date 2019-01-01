import nltk
import nltk.data
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# We will also initialize our 'english.pickle' function and give it a short name

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

"""message_text = '''The person born with Taurus as the Ascendant will have plumply thighs and a big face He will be engaged in agricultural ventures He will be happy in the middle and last portions of his life He will be fond of enjoying young women He will be of sacrificing and forgiving nature will be capable of endowing hardships and will possess cattle He will have marks or moles on the back face and side.
If the Sun is in 6th the native will be very libidinous will have powerful digestive fire capable of digesting fast be strong affluent famous for virtues and be either a king or an Army chief.	
Should the Moon be in 2nd  the native will enjoy incomparable happiness and friends and be wealthy If the said Moon be Full the native will be very affluent and will speak less.	
If Mars occupies the 5th    the native will be devoid of happiness wealth and sons be fickle minded be a talebearer  will incur evils be wicked distressed and mean.	
If Mercury occupies the 8th   the native will win famous names title be strong long lived will support his family and be equal to a king or will become a justice.
If Jupiter is in the 6th  the native will lack digestive fire and masculine virile be humiliated weak indolent will become famous on account of females will destroy his enemies and be widely famous.
If Venus occupies the 6th  the native will greatly dislike his wife will have many foes  be devoid of wealth be very much startled and be mean.
If Saturn occupies the 8th the native will suffer from leprosy and fistula in the anus or pudendum will have short life and will fail in his undertakings.	
If the Sun be in the 6th house the native will become a king He will earn renown and will be equipped with praiseworthy qualities He will be wealthy and capable of overcoming his enemies.
If the Moon be posited in the 2nd house the person born will be a man of learning sweet in speech and wealthy He will have a defective limb and be sensuous.
The person concerned will have no children and will face many disasters should the Mars happen to occupy the 5th house at birth The native will be a talebearer and without enough intelligence.
Mercury occupying the 7th house makes the native learned decently dressed He will have all greatness and a wealthy woman as his wife.
If Jupiter occupies the 6th house at birth the native will destroy his enemies but he will be lazy and will be humiliated He will be clever and well versed in the recitation and utility of Mantras.
With Venus posited in the 6th house at birth the native will have no enemies but he will be devoid of wealth He will develop ilicit relations with several young girls but will not enjoy happiness.
Saturn occupying the 8th house at birth will make the native unclean afflicted with piles devoid of wealth of cruel disposition hungry and will be avoided by his friends.
When Rahu is in the 3rd house at birth the native will be proud inimical towards his co-born wealthy longlived and strongwilled.
In the 9th house at birth makes the native indulge in sinful and unrighteous actions He will be deprived of his father will be unfortunate poverty stricken and will defame others.	
Moon in Punarvasu	Punarvasu Religious endurance happy good dull sickly thirsty and pleased with small gifts.	
If the Sun and Jupiter be together one will be virtuous be a minister of king will gain through friends be with good mind and be a preceptor.
If the Sun and Venus be together one will be skillful in use of weapons be mighty weaksighted in old age will be able to amuse the public and will have abundant money earned through women.	
One who has Jupiter and Venus together at birth will live by education and arguments will follow a highly virtuous path will have accurate conception or notion of things and will have a supreme wife
Sun Jupiter Venus	Should Venus Jupiter and the Sun be together at birth the native will be weak sighted bold intelligent indigent be a minister and be devoted to others` jobs.
all planets in 5 signs	PASA YOGA One born with pasa Yoga will be bonded be attached to work worldly in disposition will talk too much will not have good qualities and will have many servants.	
 no planet (excepting Sun) in the 2nd and 12th from the Moon	The native with Kemadruma Yoga will be deprived of life drinks food residence robes and friends though he may belong to regal scion He will suffer from poverty grief sickness and be dirty He will live by hard labor be wicked and be inimically disposed to one and all.
If Lagnas Lord is related to a malefic the native will be devoid of physical happiness and will be troubled by enemies if there is no benefic aspect.	
The native will be addicted to others wives and he will be a doctor If a malefic is related to the said placement by conjunction with the second Lord or by aspect the natives wife will be of questionable character.
The native will be corpulent devoid of valour will not make much efforts be not happy and will have an eye on others wives and others wealth.	
The native will be devoid of maternal happiness be given to anger be a thief and a conjurer be independent in action and be indisposed.
The native will be honourable very religious endowed with progenic happiness and be helpful to others.	
The native will have enmity with the group of his kinsmen but be friendly to others and will enjoy mediocre happiness in matters like wealth.	
The native will be honourable endowed with  virtues always delighted and endowed with all kinds of wealth.	
	The native will win over his enemies be afflicted by diseases and during childhood will incur danger through snakes and water.	
	The native will not be prosperous and will not enjoy happiness from his elder brother		The native will be devoid of acts long lived and intent on blaming others.	
	The native will be afflicted by diseases be cruel living in foreign places and troubled by enemies.		
The native will be bereft of sons and learning He will spend as well as visit shrines in order to beget a son.
 	If the Sun is in Libra at birth the native will face frustration destruction and heavy expenditure  will be intent on living in foreign places  be wicked mean be devoid of affection will live by selling gold and other metals be jealous fond of doing others` jobs will co habit with others` wives be dirty will incur royal contempt and be shameless.	
	If the Moon is in Gemini at birth one will have prominent nose and dark eyes will be skillful in the art of love poetry etc will enjoy sexual pleasures will have lines of fish in the palm will be fond of worldly enjoyments will be sinewy be very intelligent splendourous be endowed with happiness jocular disposition and eloquent speech be won over by the females will have a long body will befriend neuters and will have two mothers.	
	If Jupiter aspects the Moon in Gemini one will be a teacher of Shastras be famous truthful very beautiful honourable and be an eloquent speaker.	
	Should Saturn aspect the Moon in Gemini the subject will be devoid of relatives wife happiness and wealth and will be inimical to the public.	
Should Mars occupy Virgo at birth the subject will be worthy of honour  be never rich  be very fond of sexual union and music be soft and sweet spoken will have various kinds of expenses be not much valorous be learned will have ribs in their advanced position will fear enemies very much be skillful in Shastras and fine arts be fond of bathing make-up etc and be splendourous.
If Mercury is posited in Scorpio one will experience troubles grief and evils will hate the virtuous will be devoid of truth religion and shame be a dunce be not virtuous be a miser will cohabit with wicked women be fond of giving cruel punishments be not out spoken be interested in blameworthy jobs will incur debts will join base men and will steel other`s properties.
If Jupiter occupies Libra at birth one will be a scholar will have many sons be endowed with foreign assignments will be very affluent interested in ornaments modest will earn money through dance and drama be pleasing in appearance be splendourous learned in Sastras be superior among his colleague businessmen will honour Gods and guests and be very learned.
If Venus occupies Libra the native will acquire hard earned money be valorous endowed with superior robes etc interested in living in foreign countries will protect his own people be skillful in his duties rich meritorious famous by honouring Gods and Brahmins be a scholar and be fortunate.
If Saturn occupies Sagittarius one will be skillful in behavior teaching Vedic meanings learning and denotation he will be best placed in these respects be famous due to virtuous children family profession and his own virtues will enjoy excellent affluence in his old age will speak less will have many names and be soft in disposition.
If Saturn is in Sagittarius or Pisces and is aspected by the Moon one will be bereft of mother will have two names and be endowed with wife children and wealth.
If Saturn is in Sagittarius or Pisces and is aspected by Mars one will be troubled by windy diseases will dislike people be sinful mean blameworthy etc
One born under Ubhayachari Yoga will have forebearance will be very fortunate even bodied firm profoundly strong not very tall full of everything learned  happy will have many servants will protect his relatives be equal to a king ever enthusiastic and will enjoy all pleasures.
 Mercury causing this Yoga indicates that the native will be a servant will suffer penury be soft spoken and be modest He will be bashful.
 The Vasi Yoga caused by Mars indicates that the subject will be victorious in war famous and will live with his own fortunes.	
Happy strong good natured invincible	
Success after pressures or someone else`s losses	
	
	
If Dhuma is in Labha Bhava the native will be endowed with wealth grains and gold be beautiful will have knowledge of arts be modest and be skilful in singing. 
If Vyatipata is in Vyaya Bhava the native will be given to anger associated with many activities disabled irreligious and hate his own relatives.	
If Parivesha is in Ari Bhava the native will be famous and wealthy be endowed with sons and pleasures be helpful to all and will conquer his enemies.	
If Chapa is in Putra Bhava  the native will be splendourous far sighted pious affable and will acquire prosperity in all his undertakings
If Upaketu is in Putra Bhava the native will be happy will enjoy pleasures be versed in arts skilled in expedients intelligent eloquent and will respect elders.
If Gulika is in Putra Bhava the native will not be praise worthy be poor short lived spiteful mean be a eunuch be subdued by his wife and be a heterodox.

.'''"""
#message_text=input("Enter a String")

def NLP(message_text):
    sentences = tokenizer.tokenize(message_text)
    # We add the additional step of iterating through the list of sentences and calculating and printing polarity scores for each one.
    pos=[]
    neg=[]
    neu=[]
    x=1
    for sentence in sentences:
        x+=1 
        print(sentence)
        scores = sid.polarity_scores(sentence)
        neg.append(scores["neg"])
        neu.append(scores["neu"])
        pos.append(scores["pos"])
        for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]), end='')
        print()
    #print("Compound Percentage: ",(a/x))
    b=np.mean(np.array(neg))
    c=np.mean(np.array(neu))
    d=np.mean(np.array(pos))
    #return (b,c,d)
    '''print("Negative Percentage: ",(b*100))
    print("Neutral Percentage: ",(c*100))
    print("Positive Percentage: ",(d*100))'''
    return(b,c,d)
# The tokenize method breaks up the paragraph into a list of strings. In this example, note that the tokenizer is confused by the absence of spaces after periods and actually fails to break up sentences in two instances. How might you fix that?
#message_text=input()
#NLP(message_text)









