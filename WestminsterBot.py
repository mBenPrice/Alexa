"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------


def get_confession(first, chap, start, stop):
    limits = {
     1:10,
     2:3,
     3:8,
     4:2,
     5:7,
     6:6,
     7:6,
     8:8,
     9:5,
     10:4,
     11:6,
     12:1,
     13:3,
     14:3,
     15:6,
     16:7,
     17:3,
     18:4,
     19:7,
     20:4,
     21:8,
     22:7,
     23:4,
     24:6,
     25:6,
     26:3,
     27:5,
     28:7,
     29:8,
     30:4,
     31:4,
     32:3,
     33:3}
    doc = {
    1: {
        0: 'Chapter 1. Of the Holy Scripture',
        1:'Although the light of nature, and the works of creation and '
          'providence, do so far manifest the goodness, wisdom, and power of '
          'God, as to leave men inexcusable; yet are they not sufficient to '
          'give that knowledge of God, and of his will, which is necessary '
          'unto salvation; therefore it pleased the Lord, at sundry times, and '
          'in divers manners, to reveal himself, and to declare that his will '
          'unto his Church; and afterwards for the better preserving and '
          'propagating of the truth, and for the more sure establishment and '
          'comfort of the Church against the corruption of the flesh, and the '
          'malice of Satan and of the world, to commit the same wholly unto '
          'writing; which maketh the holy Scripture to be most necessary; '
          "those former ways of God's revealing his will unto his people being "
          'now ceased.',
         2:
          'Under the name of holy Scripture, or the Word of God written, '
          'are now contained all the Books of the Old and New Testament, which '
          'are these: Of the Old Testament: Genesis, Exodus, Leviticus, '
          'Numbers, Deuteronomy, Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 '
          'Kings 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther, '
          'Job, Psalm, Proverbs, Ecclesiastes, Song of Solomon, Isaiah, '
          'Jeremiah, Lamentations, Ezekiel, Daniel, Hosea, Joel, Amos, '
          'Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, '
          'Zechariah, Malachi. Of the New Testament: The Gospels according to '
          "Matthew, Mark, Luke, John, The Acts of the Apostles, Paul's "
          'Epistles to the Romans, 1 Corinthians, 2 Corinthians, Galatians, '
          'Ephesians, Philippians, Colossians, 1 Thessalonians, 2 '
          'Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon, Hebrews, '
          'James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude, Revelation. '
          'All which are given by inspiration of God, to be the rule of faith '
          'and life.',
         3:
          'The books commonly called Apocrypha, not being of divine '
          'inspiration, are no part of the Canon of Scripture; and therefore '
          'are of no authority in the Church of God, nor to be any otherwise '
          'approved, or made use of, than other human writings.',
         4:
          'The authority of the holy Scripture, for which it ought to be '
          'believed and obeyed, dependeth not upon the testimony of any man or '
          'Church, but wholly upon God (who is truth itself), the Author '
          'thereof; and therefore it is to be received, because it is the Word '
          'of God.',
         5:
          'We may be moved and induced by the testimony of the Church to an '
          'high and reverent esteem of the holy Scripture; and the '
          'heavenliness of the matter, the efficacy of the doctrine, the '
          'majesty of the style, the consent of all the parts, the scope of '
          'the whole (which is to give all glory to God), the full discovery '
          "it makes of the only way of man's salvation, the many other "
          'incomparable excellencies, and the entire perfection thereof, are '
          'arguments whereby it doth abundantly evidence itself to be the Word '
          'of God; yet, notwithstanding, our full persuasion and assurance of '
          'the infallible truth and divine authority thereof, is from the '
          'inward work of the Holy Spirit, bearing witness by and with the '
          'Word in our hearts.',
         6:
          'The whole counsel of God, concerning all things necessary for '
          "his own glory, man's salvation, faith, and life, is either "
          'expressly set down in Scripture, or by good and necessary '
          'consequence may be deduced from Scripture: unto which nothing at '
          'any time is to be added, whether by new revelations of the Spirit, '
          'or traditions of men. Nevertheless we acknowledge the inward '
          'illumination of the Spirit of God to be necessary for the saving '
          'understanding of such things as are revealed in the Word; and that '
          'there are some circumstances concerning the worship of God, and the '
          'government of the Church, common to human actions and societies, '
          'which are to be ordered by the light of nature and Christian '
          'prudence, according to the general rules of the Word, which are '
          'always to be observed.',
         7:
          'All things in Scripture are not alike plain in themselves, nor '
          'alike clear unto all; yet those things which are necessary to be '
          'known, believed, and observed, for salvation, are so clearly '
          'propounded and opened in some place of Scripture or other, that not '
          'only the learned, but the unlearned, in a due use of the ordinary '
          'means, may attain unto a sufficient understanding of them.',
         8:
          'The Old Testament in Hebrew (which was the native language of '
          'the people of God of old), and the New Testament in Greek (which, at '
          'the time of the writing of it, was most generally known to the nations), '
          'being immediately inspired by God, and, by His singular care and '
          'providence, kept pure in all ages, are therefore authentical; so as, in '
          'all controversies of religion, the Church is finally to appeal unto them. '
          'But, because these original tongues are not known to all the people of God, '
          'who have right unto, and interest in the Scriptures, and are commanded, in '
          'the fear of God, to read and search them, therefore they are to be translated '
          'in to the vulgar language of every nation unto which they come, that, the '
          'Word of God dwelling plentifully in all, they may worship Him in an '
          'acceptable manner; and, through patience and comfort of the Scriptures, may '
          'have hope.',
         9:
          'The infallible rule of interpretation of Scripture, is the '
          'Scripture itself; and therefore, when there is a question about the '
          'true and full sense of any scripture (which is not manifold, but '
          'one), it may be searched and known by other places that speak more '
          'clearly.',
         10:
          'The Supreme Judge, by which all controversies of religion are to '
          'be determined, and all decrees of councils, opinions of ancient '
          'writers, doctrines of men, and private spirits, are to be examined, '
          'and in whose sentence we are to rest, can be no other but the Holy '
          'Spirit speaking in the Scripture.'},
     2: {
         0:
          'Chapter 2. Of God, and of the Holy Trinity',
         1:
          'There is but one only living and true God, who is infinite in '
          'being and perfection, a most pure spirit, invisible, without body, '
          'parts, or passions, immutable, immense, eternal, incomprehensible, '
          'almighty, most wise, most holy, most free, most absolute, working '
          'all things according to the counsel of his own immutable and most '
          'righteous will, for his own glory, most loving, gracious, merciful, '
          'long-suffering, abundant in goodness and truth, forgiving iniquity, '
          'transgression, and sin; the rewarder of them that diligently seek '
          'him; and withal most just and terrible in his judgments; hating all '
          'sin; and who will by no means clear the guilty.',
         2:
          'God hath all life, glory, goodness, blessedness, in and of '
          'himself; and is alone in and unto himself all-sufficient, not '
          'standing in need of any creatures which he hath made, nor deriving '
          'any glory from them, but only manifesting his own glory in, by, '
          'unto, and upon them; he is the alone foundation of all being, of '
          'whom, through whom, and to whom, are all things; and hath most '
          'sovereign dominion over them, to do by them, for them, or upon '
          'them, whatsoever himself pleaseth. In his sight all things are open '
          'and manifest; his knowledge is infinite, infallible, and '
          'independent upon the creature; so as nothing is to him contingent '
          'or uncertain. He is most holy in all his counsels, in all his '
          'works, and in all his commands. To him is due from angels and men, '
          'and every other creature, whatsoever worship, service, or obedience '
          'he is pleased to require of them.',
         3:
          'In the unity of the Godhead there be three Persons of one '
          'substance, power, and eternity: God the Father, God the Son, and '
          'God the Holy Ghost. The Father is of none, neither begotten nor '
          'proceeding; the Son is eternally begotten of the Father; the Holy '
          'Ghost eternally proceeding from the Father and the Son.'},
     3: {
         0:
          "Chapter 3. Of God's Eternal Decree",
         1:
          'God from all eternity did by the most wise and holy counsel of '
          'his own will, freely and unchangeably ordain whatsoever comes to '
          'pass; yet so as thereby neither is God the author of sin; nor is '
          'violence offered to the will of the creatures, nor is the liberty '
          'or contingency of second causes taken away, but rather established.',
         2:
          'Although God knows whatsoever may or can come to pass, upon all '
          'supposed conditions; yet hath he not decreed any thing because he '
          'foresaw it as future, as that which would come to pass, upon such '
          'conditions.',
         3:
          'By the decree of God, for the manifestation of his glory, some '
          'men and angels are predestinated unto everlasting life, and others '
          'foreordained to everlasting death.',
         4:
          'These angels and men, thus predestinated and foreordained, are '
          'particularly and unchangeably designed; and their number is so '
          'certain and definite that it can not be either increased or '
          'diminished.',
         5:
          'Those of mankind that are predestinated unto life, God, before '
          'the foundation of the world was laid, according to his eternal and '
          'immutable purpose, and the secret counsel and good pleasure of his '
          'will, hath chosen in Christ, unto everlasting glory, out of his '
          'free grace and love alone, without any foresight of faith or good '
          'works, or perseverance in either of them, or any other thing in the '
          'creature, as conditions, or causes moving him thereunto; and all to '
          'the praise of his glorious grace.',
         6:
          'As God hath appointed the elect unto glory, so hath he, by the '
          'eternal and most free purpose of his will, foreordained all the '
          'means thereunto. Wherefore they who are elected being fallen in '
          'Adam are redeemed by Christ, are effectually called unto faith in '
          'Christ by his Spirit working in due season; are justified, adopted, '
          'sanctified, and kept by his power through faith unto salvation. '
          'Neither are any other redeemed by Christ, effectually called, '
          'justified, adopted, sanctified, and saved, but the elect only.',
         7:
          'The rest of mankind, God was pleased, according to the '
          'unsearchable counsel of his own will, whereby he extendeth or '
          'withholdeth mercy as he pleaseth, for the glory of his sovereign '
          'power over his creatures, to pass by, and to ordain them to '
          'dishonor and wrath for their sin, to the praise of his glorious '
          'justice.',
         8:
          'The doctrine of this high mystery of predestination is to '
          'be handled with special prudence and care, that men, attending the '
          'will of God revealed in His Word, and yielding obedience thereunto, '
          'may, from the certainty of their effectual vocation, be assured of '
          'their eternal election. So shall this doctrine afford matter of '
          'praise, reverence, and admiration of God; and of humility, diligence, '
          'and abundant consolation to all that sincerely obey the Gospel.'},
     4: {
         0:
          'Chapter 4. Of Creation',
         1:
          'It pleased God the Father, Son, and Holy Ghost, for the '
          'manifestation of the glory of his eternal power, wisdom, and '
          'goodness, in the beginning, to create or make of nothing the world, '
          'and all things therein, whether visible or invisible, in the space '
          'of six days, and all very good.',
         2:
          'After God had made all other creatures, he created man, male '
          'and female, with reasonable and immortal souls, endued with '
          'knowledge, righteousness, and true holiness after his own image, '
          'having the law of God written in their hearts, and power to fulfill '
          'it; and yet under a possibility of transgressing, being left to the '
          'liberty of their own will, which was subject unto change. Besides '
          'this law written in their hearts, they received a command not to '
          'eat of the tree of the knowledge of good and evil; which while they '
          'kept were happy in their communion with God, and had dominion over '
          'the creatures.'},
     5: {
         0:
          'Chapter 5. Of Providence',
         1:
          'God, the great Creator of all things, doth uphold, direct '
          'dispose, and govern all creatures, actions, and things, from the '
          'greatest even to the least, by his most wise and holy providence, '
          'according to his infallible foreknowledge, and the free and '
          'immutable counsel of his own will, to the praise of the glory of '
          'his wisdom, power, justice, goodness, and mercy.',
         2:
          'Although in relation to the foreknowledge and decree of God, '
          'the first cause, all things come to pass immutably and infallibly, '
          'yet, by the same providence, he ordereth them to fall out according '
          'to the nature of second causes, either necessarily, freely, or '
          'contingently.',
         3:
          'God, in his ordinary providence, maketh use of means, yet is '
          'free to work without, above, and against them, at his pleasure.',
         4:
          'The almighty power, unsearchable wisdom, and infinite goodness '
          'of God, so far manifest themselves in his providence, that it '
          'extendeth itself even to the first Fall, and all other sins of '
          'angels and men, and that not by a bare permission, but such as hath '
          'joined with it a most wise and powerful bounding, and otherwise '
          'ordering and governing of them, in a manifold dispensation, to his '
          'own holy ends; yet so, as the sinfulness thereof proceedeth only '
          'from the creature, and not from God; who being most holy and '
          'righteous, neither is nor can be the author or approver of sin.',
         5:
          'The most wise, righteous, and gracious God, doth oftentimes '
          'leave for a season his own children to manifold temptations and the '
          'corruption of their own hearts, to chastise them for their former '
          'sins, or to discover unto them the hidden strength of corruption '
          'and deceitfulness of their hearts, that they may be humbled; and to '
          'raise them to a more close and constant dependence for their '
          'support upon himself, and to make them more watchful against all '
          'future occasions of sin, and for sundry other just and holy ends.',
         6:
          'As for those wicked and ungodly men whom God, as a righteous '
          'judge, for former sins, doth blind and harden; from them he not '
          'only withholdeth his grace, whereby they might have been '
          'enlightened in their understandings, and wrought upon their hearts; '
          'but sometimes also withdraweth the gifts which they had; and '
          'exposeth them to such objects as their corruption makes occasion of '
          'sin; and withal, gives them over to their own lusts, the '
          'temptations of the world, and the power of Satan; whereby it comes '
          'to pass that they harden themselves, even under those means which '
          'God useth for the softening of others.',
         7:
          'As the providence of God doth, in general, reach to all '
          'creatures, so, after a most special manner, it taketh care of his '
          'Church, and disposeth all things to the good thereof.'},
     6: {
         0:
          'Chapter 6. Of the Fall of Man, of Sin, and of the Punishment thereof',
         1:
          'Our first parents, begin seduced by the subtlety and temptations '
          'of Satan, sinned in eating the forbidden fruit. This their sin God '
          'was pleased, according to his wise and holy counsel, to permit, '
          'having purposed to order it to his own glory.',
         2:
          'By this sin they fell from their original righteousness and '
          'communion with God, and so became dead in sin, and wholly defiled '
          'in all the faculties and parts of soul and body.',
         3:
          'They being the root of mankind, the guilt of this sin was '
          'imputed, and the same death in sin and corrupted nature conveyed to '
          'all their posterity, descending from them by original generation.',
         4:
          'From this original corruption, whereby we are utterly '
          'indisposed, disabled, and made opposite to all good, and wholly '
          'inclined to all evil, do proceed all actual transgressions.',
         5:
          'This corruption of nature, during this life, doth remain in '
          'those that are regenerated; and although it be through Christ '
          'pardoned and mortified, yet both itself, and all the motions '
          'thereof, are truly and properly sin.',
         6:
          'Every sin, both original and actual, being a transgression of '
          'the righteous law of God, and contrary thereunto, doth, in its own '
          'nature, bring guilt upon the sinner, whereby he is bound over to '
          'the wrath of God, and curse of the law, and so made subject to '
          'death, with all miseries spiritual, temporal, and eternal.'},
     7: {
         0:
          "Chapter 7. Of God's Covenant with Man",
         1:
          'The distance between God and the creature is so great, that '
          'although reasonable creatures do owe obedience unto him as their '
          'Creator, yet they could never have any fruition of him, as their '
          'blessedness and reward, but by some voluntary condescension on '
          "God's part, which he hath been pleased to express by way of "
          'covenant.',
         2:
          'The first covenant made with man was a covenant of works, '
          'wherein life was promised to Adam, and in him to his posterity, '
          'upon condition of perfect and personal obedience.',
         3:
          'Man by his fall having made himself incapable of life by that '
          'covenant, the Lord was pleased to make a second, commonly called '
          'the covenant of grace: wherein he freely offered unto sinners life '
          'and salvation by Jesus Christ, requiring of them faith in him, that '
          'they may be saved, and promising to give unto all those that are '
          'ordained unto life, his Holy Spirit, to make them willing and able '
          'to believe.',
         4:
          'This covenant of grace is frequently set forth in the Scripture '
          'by the name of a testament, in reference to the death of Jesus '
          'Christ, the testator, and to the everlasting inheritance, with all '
          'things belonging to it, therein bequeathed.',
         5:
          'This covenant was differently administered in the time of the '
          'law, and in the time of the gospel: under the law it was '
          'administered by promises, prophecies, sacrifices, circumcision, the '
          'paschal lamb, and other types and ordinances delivered to the '
          'people of the Jews, all fore-signifying Christ to come, which were '
          'for that time sufficient and efficacious, through the operation of '
          'the Spirit, to instruct and build up the elect in faith in the '
          'promised Messiah, by whom they had full remission of sins, and '
          'eternal salvation, and is called the Old Testament.',
         6:
          'Under the gospel, when Christ the substance was exhibited, the '
          'ordinances in which this covenant is dispensed, are the preaching '
          'of the Word, and the administration of the sacraments of Baptism '
          "and the Lord's Supper; which, though fewer in number, and "
          'administered with more simplicity and less outward glory, yet in '
          'them it is held forth in more fullness, evidence, and spiritual '
          'efficacy, to all nations, both Jews and Gentiles; and is called the '
          'New Testament. There are not, therefore, two covenants of grace '
          'differing in substance, but one and the same under various '
          'dispensations.'},
     8: {
         0:
          'Chapter 8. Of Christ the Mediator',
         1:
          'It pleased God, in his eternal purpose, to choose and ordain the '
          'Lord Jesus, his only-begotten Son, to be the Mediator between God '
          'and men, the prophet, priest, and king; the head and Savior of the '
          'Church, the heir or all things, and judge of the world; unto whom '
          'he did, from all eternity, give a people to be his seed, and to be '
          'by him in time redeemed, called, justified, sanctified, and '
          'glorified.',
         2:
          'The Son of God, the second Person in the Trinity, being very '
          'and eternal God, of one substance, and equal with the Father, did, '
          "when the fullness of time was come, take upon him man's nature, "
          'with all the essential properties and common infirmities thereof; '
          'yet without sin: being conceived by he power of the Holy Ghost, in '
          'the womb of the Virgin Mary, of her substance. So that two whole, '
          'perfect, and distinct natures, the Godhead and the manhood, were '
          'inseparably joined together in one person, without conversion, '
          'composition, or confusion. Which person is very God and very man, '
          'yet one Christ, the only Mediator between God and man.',
         3:
          'The Lord Jesus in his human nature thus united to the divine, '
          'was sanctified and anointed with the Holy Spirit above measure; '
          'having in him all the treasures of wisdom and knowledge, in whom it '
          'pleased the Father that all fullness should dwell: to the end that '
          'being holy, harmless, undefiled, and full of grace and truth, he '
          'might be thoroughly furnished to execute the office of a Mediator '
          'and Surety. Which office he took not unto himself, but was '
          'thereunto called by his Father; who put all power and judgment into '
          'his hand, and gave him commandment to execute the same.',
         4:
          'This office the Lord Jesus did most willingly undertake, which, '
          'that he might discharge, he was made under the law, and did '
          'perfectly fulfill it; endured most grievous torments immediately in '
          'his soul, and most painful sufferings in his body; was crucified '
          'and died; was buried, and remained under the power of death, yet '
          'saw no corruption. On the third day he arose from the dead, with '
          'the same body in which he suffered; with which also he ascended '
          'into heaven, and there sitteth at the right hand of his Father, '
          'making intercession; and shall return to judge men and angels, at '
          'the end of the world.',
         5:
          'The Lord Jesus, by his perfect obedience and sacrifice of '
          'himself, which he through the eternal Spirit once offered up unto '
          'God, hath fully satisfied the justice of his Father; and purchased '
          'not only reconciliation, but an everlasting inheritance in the '
          'kingdom of heaven, for all those whom the Father hath given unto '
          'him.',
         6:
          'Although the work of redemption was not actually wrought by '
          'Christ till after his incarnation, yet the virtue, efficacy, and '
          'benefits thereof were communicated into the elect, in all ages '
          'successively from the beginning of the world, in and by those '
          'promises, types, and sacrifices wherein he was revealed, and '
          'signified to be the seed of the woman, which should bruise the '
          "serpent's head, and the Lamb slain from the beginning of the world, "
          'being yesterday and today the same and for ever.',
         7:
          'Christ, in the work of mediation, acteth according to both '
          'natures; by each nature doing that which is proper to itself; yet '
          'by reason of the unity of the person, that which is proper to one '
          'nature is sometimes, in Scripture, attributed to the person '
          'denominated by the other nature.',
         8:
          'To all those for whom Christ has purchased redemption, He does '
          'certainly and effectually apply and communicate the same; making '
          'intercession for them, and revealing unto them, in and by the word, '
          'the mysteries of salvation; effectually persuading them by His Spirit '
          'to believe and obey, and governing their hearts by His word and Spirit; '
          'overcoming all their enemies by His almighty power and wisdom, in such '
          'manner, and ways, as are most consonant to His wonderful and unsearchable '
          'dispensation.'},
     9: {
         0:
          'Chapter 9. Of Free Will',
         1:
          'God hath endued the will of man with that natural liberty, that '
          'is neither forced, nor by any absolute necessity of nature '
          'determined to good or evil.',
         2:
          'Man, in his state of innocency, had freedom and power to will '
          'and to do that which is good and well-pleasing to God; but yet '
          'mutably, so that he might fall from it.',
         3:
          'Man, by his fall into a state of sin, hath wholly lost all '
          'ability of will to any spiritual good accompanying salvation; so as '
          'a natural man, being altogether averse from that good, and dead in '
          'sin, is not able, by his own strength, to convert himself, or to '
          'prepare himself thereunto.',
         4:
          'When God converts a sinner and translates him into the state of '
          'grace, he freeth him from his natural bondage under sin, and, by '
          'his grace alone, enables him freely to will and to do that which is '
          'spiritually good; yet so as that, by reason of his remaining '
          'corruption, he doth not perfectly, nor only, will that which is '
          'good, but doth also will that which is evil.',
         5:
          'The will of man is made perfectly and immutable free to good '
          'alone, in the state of glory only.'},
     10: {
         0:
          'Chapter 10. Of Effectual Calling',
         1:
           'All those whom God hath predestinated unto life, and those '
           'only, he is pleased, in his appointed and accepted time, '
           'effectually to call, by his Word and Spirit, out of that state of '
           'sin and death in which they are by nature, to grace and salvation '
           'by Jesus Christ: enlightening their minds, spiritually and '
           'savingly, to understand the things of God, taking away their heart '
           'of stone, and giving unto them an heart of flesh; renewing their '
           'wills, and by his almighty power determining them to that which is '
           'good; and effectually drawing them to Jesus Christ; yet so as they '
           'come most freely, being made willing by his grace.',
          2:
           "This effectual call is of God's free and special grace alone, "
           'not from any thing at all foreseen in man, who is altogether '
           'passive therein, until, being quickened and renewed by the Holy '
           'Spirit, he is thereby enabled to answer this call, and to embrace '
           'the grace offered and conveyed in it.',
          3:
           'Elect infants, dying in infancy, are regenerated and saved by '
           'Christ through the Spirit, who worketh when, and where, and how he '
           'pleaseth. So also are all other elect persons who are incapable of '
           'being outwardly called by the ministry of the Word.',
          4:
           'Others, not elected, although they may be called by the '
           'ministry of the Word, and may have some common operations of the '
           'Spirit, yet they never truly come to Christ, and therefore can not '
           'be saved: much less can men, not professing the Christian '
           'religion, be saved in any other way whatsoever, be they never so '
           'diligent to frame their lives according to the light of nature, '
           'and the law of that religion they do profess; and to assert and '
           'maintain that they may is without warrant of the Word of God.'},
     11: {
         0:
          'Chapter 11. Of Justification',
         1:
           'Those whom God effectually calleth, he also freely justifieth: '
           'not by infusing righteousness into them, but by pardoning their '
           'sins, and by accounting and accepting their persons as righteous; '
           'not for any thing wrought in them, or done by them, but for '
           "Christ's sake alone; not by imputing faith itself, the act of "
           'believing, or any other evangelical obedience to them, as their '
           'righteousness; but by imputing the obedience and satisfaction of '
           'Christ unto them, they receiving and resting on him and his '
           'righteousness by faith; which faith they have not of themselves, '
           'it is the gift of God.',
          2:
           'Faith, thus receiving and resting on Christ and his '
           'righteousness, is the alone instrument of justification; yet is it '
           'not alone in the person justified, but is ever accompanied with '
           'all other saving graces, and is no dead faith, but worketh by love.',
          3:
           'Christ, by his obedience and death, did fully discharge the '
           'debt of all those that are thus justified, and did make a proper, '
           "real, and full satisfaction of his Father's justice in their "
           'behalf. Yet inasmuch as he was given by the Father for them, and '
           'his obedience and satisfaction accepted in their stead, and both '
           'freely, not for any thing in them, their justification is only of '
           'free grace, that both the exact justice and rich grace of God '
           'might be glorified in the justification of sinners.',
          4:
           'God did, from all eternity, decree to justify the elect; and '
           'Christ did, in the fullness of time, die for their sins and rise '
           'again for their justification; nevertheless they are not justified '
           'until the Holy Spirit doth, in due time, actually apply Christ '
           'unto them.',
          5:
           'God doth continue to forgive the sins of those that are '
           'justified; and although they can never fall from the state of '
           "justification, yet they may by their sins fall under God's "
           'Fatherly displeasure, and not have the light of his countenance '
           'restored unto them, until they humble themselves, confess their '
           'sins, beg pardon, and renew their faith and repentance.',
          6:
           'The justification of believers under the Old Testament was, in '
           'all these respect, one and the same with the justification of '
           'believers under the New Testament.'},
     12: {
         0:
           'Chapter 12. Of Adoption',
         1:
           'All those that are justified, God vouchsafes, in and for His only '
           'Son Jesus Christ, to make partakers of the grace of adoption, by which '
           'they are taken into the number, and enjoy the liberties and privileges '
           'of the children of God, have His name put upon them, receive the spirit '
           'of adoption, have access to the throne of grace with boldness, are enabled '
           'to cry, Abba, Father, are pitied, protected, provided for, and chastened '
           'by Him as by a Father: yet never cast off, but sealed to the day of '
           'redemption; and inherit the promises, as heirs of everlasting salvation.'},
     13: {
         0:
           'Chapter 13. Of Sanctification',
         1:
           'They who are effectually called and regenerated, having a new '
           'heart and a new spirit created in them, are further sanctified, '
           "really and personally, through the virtue of Christ's death and "
           'resurrection, by his Word and Spirit dwelling in them; the '
           'dominion of the whole body of sin is destroyed, and the several '
           'lusts thereof are more and more weakened and mortified, and they '
           'more and more quickened and strengthened, in all saving graces, to '
           'the practice of true holiness, without which no man shall see the '
           'Lord.',
          2:
           'This sanctification is throughout in the whole man, yet '
           'imperfect in this life: there abideth still some remnants of '
           'corruption in every part, whence ariseth a continual and '
           'irreconcilable war, the flesh lusting against the Spirit, and the '
           'Spirit against the flesh.',
          3:
           'In which war, although the remaining corruption for a time '
           'may much prevail, yet, through the continual supply of strength '
           'from the sanctifying Spirit of Christ, the regenerate part doth '
           'overcome: and so the saints grow in grace, perfecting holiness in '
           'the fear of God.'},
     14: {
         0:
           'Chapter 14. Of Saving Faith',
         1:
           'The grace of faith, whereby the elect are enabled to believe to '
           'the saving of their souls, is the work of the Spirit of Christ in '
           'their hearts; and is ordinarily wrought by the ministry of the '
           'Word: by which also, and by the administration of the sacraments, '
           'and prayer, it is increased and strengthened.',
          2:
           'By this faith, a Christian believeth to be true whatsoever is '
           'revealed in the Word, for the authority of god himself speaking '
           'therein; and acteth differently, upon that which each particular '
           'passage thereof containeth; yielding obedience to the commands, '
           'trembling at the threatenings, and embracing the promises of God '
           'for this life, and that which is to come. But the principle acts '
           'of saving faith are, accepting, receiving, and resting upon Christ '
           'alone for justification, sanctification, and eternal life, by '
           'virtue of the covenant of grace.',
          3:
           'This faith is different in degrees, weak or strong; may be '
           'often and many ways assailed and weakened, but gets the victory; '
           'growing up in many to the attainment of a full assurance through '
           'Christ, who is both the author and finisher of our faith.'},
     15: {
         0:
           'Chapter 15. Of Repentance Unto Life',
         1:
           'Repentance unto life is an evangelical grace, the doctrine '
           'whereof is to be preached by every minister of the gospel, as well '
           'as that of faith in Christ.',
          2:
           'By it a sinner, out of the sight and sense, not only of the '
           'danger, but also of the filthiness and odiousness of his sins, as '
           'contrary to the holy nature and righteous law of God, and upon the '
           'apprehension of his mercy in Christ to such as are penitent, so '
           'grieves for, and hates his sins, as to turn from them all unto '
           'God, purposing and endeavoring to walk with him in all the ways of '
           'his commandments.',
          3:
           'Although repentance be not to be rested in as any '
           'satisfaction for sin, or any cause of the pardon thereof, which is '
           "the act of God's free grace in Christ; yet is it of such necessity "
           'to all sinners, that none may expect pardon without it.',
          4:
           'As there is no sin so small but it deserves damnation; so '
           'there is no sin so great that it can bring damnation upon those '
           'who truly repent.',
          5:
           'Men ought not to content themselves with a general repentance, '
           "but it is every man's duty to endeavor to repent of his particular "
           'sins, particularly.',
          6:
           'As every man is bound to make private confession of his sins '
           'to God, praying for the pardon thereof, upon which, and the '
           'forsaking of them, he shall find mercy: so he that scandalizeth '
           'his brother, or the Church of Christ, ought to be willing, by a '
           'private or public confession and sorrow for his sin, to declare '
           'his repentance to those that are offended; who are thereupon to be '
           'reconciled to him, and in love to receive him.'},
     16: {
          0:
           'Chapter 16. Of Good Works',
          1:
           'Good works are only such as God hath commanded in his holy '
           'Word, and not such as, without the warrant thereof, are devised by '
           'men out of blind zeal, or upon any pretense of good intention.',
          2:
           "These good works, done in obedience to God's commandments, are "
           'the fruits and evidences of a true and lively faith: and by them '
           'believers manifest their thankfulness, strengthen their assurance, '
           'edify their brethren, adorn the profession of the gospel, stop the '
           'mouths of the adversaries, and glorify God, whose workmanship they '
           'are, created in Christ Jesus thereunto, that, having their fruit '
           'unto holiness, they may have the end, eternal life.',
          3:
           'Their ability to do good works is not at all of themselves, '
           'but wholly from the Spirit of Christ. And that they may be enabled '
           'thereunto, besides the graces they have already received, there is '
           'required an actual influence of the same Holy Spirit to work in '
           'them to will and to do of his good pleasure; yet are they not '
           'hereupon to grow negligent, as if they were not bound to perform '
           'any duty unless upon a special motion of the Spirit; but they '
           'ought to be diligent in stirring up the grace of God that is in '
           'them.',
          4:
           'They, who in their obedience, attain to the greatest height '
           'which is possible in this life, are so far from being able to '
           'supererogate and to do more than God requires, that they fall '
           'short of much which in duty they are bound to do.',
          5:
           'We can not, by our best works, merit pardon of sin, or eternal '
           'life, at the hand of God, because of the great disproportion that '
           'is between them and the glory to come, and the infinite distance '
           'that is between us and God, whom by them we can neither profit, '
           'nor satisfy for the debt of our former sins; but when we have done '
           'all we can, we have done but our duty, and are unprofitable '
           'servants: and because, as they are good, they proceed from his '
           'Spirit; and as they are wrought by us, they are defiled and mixed '
           'with so much weakness and imperfection that they can not endure '
           "the severity of God's judgment.",
          6:
           'Yet notwithstanding, the persons of believers being accepted '
           'through Christ, their good works also are accepted in him, not as '
           'though they were in this life wholly unblamable and unreprovable '
           "in God's sight; but that he, looking upon them in his Son, is "
           'pleased to accept and reward that which is sincere, although '
           'accompanied with many weaknesses and imperfections.',
          7:
           'Works done by unregenerate men, although for the matter of '
           'them they may be things which God commands, and of good use both '
           'to themselves and others; yet, because they proceed not from a '
           'heart purified by faith; nor are done in a right manner, according '
           'to the Word; nor to a right end, the glory of God; they are '
           'therefore sinful and can not please God, or make a man meet to '
           'receive grace from God. And yet their neglect of them is more '
           'sinful, and displeasing unto God.'},
     17: {
          0:
           'Chapter 17. Of The Perseverance of the Saints',
          1:
           'They whom God hath accepted in his Beloved, effectually called '
           'and sanctified by his Spirit, can neither totally nor finally fall '
           'away from the state of grace; but shall certainly persevere '
           'therein to the end, and be eternally saved.',
          2:
           'This perseverance of the saints depends, not upon their own '
           'free-will, but upon the immutability of the decree of election, '
           'flowing from the free and unchangeable love of God the Father; '
           'upon the efficacy of the merit and intercession of Jesus Christ; '
           'the abiding of the Spirit and of the seed of God within them; and '
           'the nature of the covenant of grace; from all which ariseth also '
           'the certainty and infallibility thereof.',
          3:
           'Nevertheless they may, through the temptations of Satan and '
           'of the world, the prevalancy of corruption remaining in them, and '
           'the neglect of the means of their perseverance, fall into grievous '
           "sins; ad for a time continue therein: whereby they incur God's "
           'displeasure, and grieve his Holy Spirit; come to be deprived of '
           'some measure of their graces and comforts; have their hearts '
           'hardened, and their consciences wounded; hurt and prevalancy '
           'others, and bring temporal judgments upon themselves.'},
     18: {
          0:
           'Chapter 18. Of the Assurance of Grace and Salvation',
          1:
           'Although hypocrites, and other unregenerate men, may vainly '
           'deceive themselves with false hopes and carnal presumptions: of '
           'being in the favor of God and estate of salvation; which hope of '
           'theirs shall perish: yet such as truly believe in the Lord Jesus, '
           'and love him in sincerity, endeavoring to walk in all good '
           'conscience before him, may in this life be certainly assured that '
           'they are in a state of grace, and may rejoice in the hope of the '
           'glory of God: which hope shall never make them ashamed.',
          2:
           'This certainty is not a bare conjectural and probably '
           'persuasion, grounded upon a fallible hope; but an infallible '
           'assurance of faith, founded upon the divine truth of the promises '
           'of salvation, the inward evidence of those graces unto which these '
           'promises are made, the testimony of the Spirit of adoption '
           'witnessing with our spirits that we are the children of God; which '
           'Spirit is the earnest of our inheritance, whereby we are sealed to '
           'the day of redemption.',
          3:
           'This infallible assurance doth not so belong to the essence '
           'of faith but that a true believer may wait long and conflict with '
           'many difficulties before he be partaker of it: yet, being enabled '
           'by the Spirit to know the things which are freely given him of '
           'God, he may, without extraordinary revelation, in the right use of '
           'ordinary means, attain thereunto. And therefore it is the duty of '
           'everyone to give all diligence to make his calling and election '
           'sure; that thereby his heart may be enlarged in peace and joy in '
           'the Holy Ghost, in love and thankfulness to God, and in strength '
           'and cheerfulness in the duties of obedience, the proper fruits of '
           'this assurance: so far is it from inclining men to looseness.',
          4:
           'True believers may have the assurance of their salvation '
           'divers ways shaken, diminished, and intermitted; as, by negligence '
           'in preserving of it; by falling into some special sin, which '
           'woundeth the conscience, and grieveth the Spirit; by some sudden '
           "or vehement temptation; by God's withdrawing the light of his "
           'countenance and suffering even such as fear him to walk in '
           'darkness and to have no light: yet are they never utterly '
           'destitute of that seed of God, and life of faith, that love of '
           'Christ and the brethren, that sincerity of heart and conscience of '
           'duty, out of which, by the operation of the Spirit, this assurance '
           'may in due time be revived, and by the which, in the meantime, '
           'they are supported from utter despair.'},
     19: {
          0:
           'Chapter 19. Of the Law of God',
          1:
           'God gave to Adam a law, as a covenant of works, by which he '
           'bound him and all his posterity to personal, entire, exact, and '
           'perpetual obedience; promised life upon the fulfilling, and '
           'threatened death upon the breach of it; and endued him with power '
           'and ability to keep it.',
          2:
           'This law, after his Fall, continued to be a perfect rule of '
           'righteousness; and, as such, was delivered by God upon mount Sinai '
           'in ten commandments, and written in two tables; the first four '
           'commandments containing our duty toward God, and the other six our '
           'duty to man.',
          3:
           'Besides this law, commonly called moral, God was pleased to '
           'give to the people of Israel, as a Church under age, ceremonial '
           'laws, containing several typical ordinances, partly of worship, '
           'prefiguring Christ, his graces, actions, sufferings, and benefits; '
           'and partly holding forth divers instructions of moral duties. All '
           'which ceremonial laws are now abrogated under the New Testament.',
          4:
           'To them also, as a body politic, he gave sundry judicial laws, '
           'which expired together with the state of that people, not obliging '
           'any other, now, further than the general equity thereof may '
           'require.',
          5:
           'The moral law doth forever bind all, as well justified persons '
           'as others, to the obedience thereof; and that not only in regard '
           'of the matter contained in it, but also in respect of the '
           'authority of God the Creator who gave it. Neither doth Christ in '
           'the gospel any way dissolve, but much strengthen, this obligation.',
          6:
           'Although true believers be not under the law as a covenant of '
           'works, to be thereby justified or condemned; yet is it of great '
           'use to them, as well as to others; in that, as a rule of life, '
           'informing them of the will of God and their duty, it directs and '
           'binds them to walk accordingly; discovering also the sinful '
           'pollutions of their nature, hearts, and lives; so as, examining '
           'themselves thereby, they may come to further conviction of, '
           'humiliation for, and hatred against sin; together with a clearer '
           'sight of the need they have of Christ, and the perfection of his '
           'obedience. It is likewise of use to the regenerate, to restrain '
           'their corruptions, in that it forbids sin, and the threatenings of '
           'it serve to show what even their sins deserve, and what '
           'afflictions in this life they may expect for them, although freed '
           'from the curse thereof threatened in the law. The promises of it, '
           "in like manner, show them God's approbation of obedience, and what "
           'blessings they may expect upon the performance thereof; although '
           'not as due to them by the law as a covenant of works: so as a '
           "man's doing good, and refraining from evil, because the law "
           'encourageth to the one, and deterreth from the other, is no '
           'evidence of his being under the law, and not under grace.',
          7:
           'Neither are the forementioned uses of the law contrary to the '
           'grace of the gospel, but do sweetly comply with it: the Spirit of '
           'Christ subduing and enabling the will of man to do that freely and '
           'cheerfully, which the will of God, revealed in the law, requireth '
           'to be done.'},
     20: {
          0:
           'Chapter 20. Of Christian Liberty, and Liberty of Conscience',
          1:
           'The liberty which Christ hath purchased for believers under the '
           'gospel consists in their freedom from the guilt of sin, the '
           'condemning wrath of God, the curse of the moral law; and in their '
           'being delivered from this present evil world, bondage to Satan, '
           'and dominion of sin, from the evil of afflictions, the sting of '
           'death, the victory of the grave, and everlasting damnation; as '
           'also in their free access to God, and their yielding obedience '
           'unto him, not out of slavish fear, but a childlike love, and a '
           'willing mind. All which were common also to believers under the '
           'law; but under the New Testament the liberty of Christians is '
           'further enlarged in their freedom from the yoke of the ceremonial '
           'law, to which the Jewish Church was subjected; and in greater '
           'boldness of access to the throne of grace, and in fuller '
           'communications of the free Spirit of God, than believers under the '
           'law did ordinarily partake of.',
          2:
           'God alone is Lord of the conscience, and hath left it free '
           'from the doctrines and commandments of men which are in any thing '
           'contrary to his Word, or beside it in matters of faith or worship. '
           'So that to believe such doctrines, or to obey such commandments '
           'out of conscience, is to betray true liberty of conscience; and '
           'the requiring an implicit faith, and an absolute and blind '
           'obedience, is to destroy liberty of conscience, and reason also.',
          3:
           'They who, upon pretense of Christian liberty, do practice any '
           'sin, or cherish any lust, do thereby destroy the end of Christian '
           'liberty; which is, that, being delivered out of the hands of our '
           'enemies, we might serve the Lord without fear, in holiness and '
           'righteousness before him, all the days of our life.',
          4:
           'And because the powers which God hath ordained, and the '
           'liberty which Christ hath purchased, are not intended by God to '
           'destroy, but mutually to uphold and preserve one another; they '
           'who, upon pretence of Christian liberty, shall oppose any lawful '
           'power, or the lawful exercise of it, whether it be civil or '
           'ecclesiastical, resist the ordinance of God. And, for their '
           'publishing of such opinions, or maintaining of such practices, as '
           'are contrary to the light of nature, or to the known principles of '
           'Christianity, whether concerning faith, worship, or conversation; '
           'or, to the power of godliness; or, such erroneous opinions or '
           'practices, as either in their own nature, or in the manner of '
           'publishing or maintaining them, are destructive to the external '
           'peace and order which Christ hath established in the Church, they '
           'may lawfully be called to account, and proceeded against by the '
           'censures of the Church, and by the power of the civil magistrate.'},
     21: {
          0:
           'Chapter 21. Of Religious Worship and the Sabbath-day',
          1:
           'The light of nature showeth that there is a God, who hath '
           'lordship and sovereignty over all; is good, and doeth good unto '
           'all; and is therefore to be feared, loved, praised, called upon, '
           'trusted in, and served with all the hearth, and with all the soul, '
           'and with all the might. But the acceptable way of worshipping the '
           'true God is instituted by himself, and so limited by his own '
           'revealed will, that he may not be worshipped according to the '
           'imaginations and devices of men, or the suggestions of Satan, '
           'under any visible representation or any other way not prescribed '
           'in the holy Scripture.',
          2:
           'Religious worship is to be given to God, the Father, Son, and '
           'Holy Ghost; and to him alone: not to angels, saints, or any other '
           'creature: and since the Fall, not without a Mediator; nor in the '
           'mediation of any other but of Christ alone.',
          3:
           'Prayer with thanksgiving, being one special part of religious '
           'worship, is by God required of all men; and that it may be '
           'accepted, it is to be made in the name of the Son, by the help of '
           'his Holy Spirit, according to his will, with understanding, '
           'reverence, humility, fervency, faith, love, and perseverance; and, '
           'if vocal, in a known tongue.',
          4:
           'Prayer is to be made for things lawful, and for all sorts of '
           'men living, or that shall live hereafter; but not for the dead, '
           'nor for those of whom it may be known that they have sinned the '
           'sin unto death.',
          5:
           'The reading of the Scriptures with godly fear; the sound '
           'preaching, and conscionable hearing of the Word, in obedience unto '
           'God with understanding, faith, and reverence; singing of psalms '
           'with grace in the heart; as, also, the due administration and '
           'worthy receiving of the sacraments instituted by Christ; are all '
           'parts of the ordinary religious worship of God: besides religious '
           'oaths, and vows, solemn fastings, and thanksgivings upon special '
           'occasion; which are, in their several times and seasons, to be '
           'used in an holy and religious manner.',
          6:
           'Neither prayer, nor any other part of religious worship, is '
           'now, under the gospel, either tied unto, or made more acceptable '
           'to, any place in which it is performed, or towards which it is '
           'directed: but God is to be worshipped everywhere in spirit and in '
           'truth; as in private families daily, and in secret each one by '
           'himself, so more solemnly in the public assemblies, which are not '
           'carelessly or willfully to be neglected or forsaken, when God, by '
           'his Word or providence, calleth thereunto.',
          7:
           'As it is of the law of nature, that, in general, a due '
           'proportion of time be set apart for the worship of God; so, in his '
           'Word, by a positive, moral, and perpetual commandment, binding all '
           'men in all ages, he hath particularly appointed one day in seven '
           'for a Sabbath, to be kept holy unto him: which, from the beginning '
           'of the world to the resurrection of Christ, was the last day of '
           'the week; and, from the resurrection of Christ, was changed into '
           "the first day of the week, which in Scripture is called the Lord's "
           'Day, and is to be continued to the end of the world as the '
           'Christian Sabbath.',
          8:
           'This Sabbath is to be kept holy unto the Lord when men, after '
           'a due preparing of their hearts, and ordering of their common affairs '
           'beforehand, do not only observe an holy rest all the day from their '
           'own works, words, and thoughts about their worldly employments and '
           'recreations, but also are taken up the whole time in the public and '
           'private exercises of His worship, and in the duties of necessity and '
           'mercy.'},
     22: {
         0:
          'Chapter 22. Of Lawful Oaths and Vows',
         1:
           'A lawful oath is a part of religious worship, wherein upon just '
           'occasion, the person swearing solemnly calleth God to witness what '
           'he asserteth or promiseth; and to judge him according to the truth '
           'or falsehood of what he sweareth.',
          2:
           'The name of God only is that by which men ought to swear, and '
           'therein it is to be used with all holy fear and reverence; '
           'therefore to swear vainly or rashly by that glorious and dreadful '
           'name, or to swear at all by any other thing, is sinful, and to be '
           'abhorred. Yet, as, in matters of weight and moment, an oath is '
           'warranted by the Word of God, under the New Testament, as well as '
           'under the Old, so a lawful oath, being imposed by lawful '
           'authority, in such matters ought to be taken.',
          3:
           'Whosoever taketh an oath ought duly to consider the '
           'weightiness of so solemn an act, and therein to avouch nothing but '
           'what he is fully persuaded is the truth. Neither may any man bind '
           'himself by oath to any thing but what is good and just, and what '
           'he believeth so to be, and what he is able and resolved to '
           'perform. Yet it is a sin to refuse an oath touching any thing that '
           'is good and just, being imposed by lawful authority.',
          4:
           'An oath is to be taken in the plain and common sense of the '
           'words, without equivocation or mental reservation. It can not '
           'oblige to sin; but in any thing not sinful, being taken, it binds '
           "to performance, although to a man's own hurt: nor is it to be "
           'violated, although made to heretics or infidels.',
          5:
           'A vow is of the like nature with a promissory oath, and ought '
           'to be made with the like religious care, and to be performed with '
           'the like faithfulness.',
          6:
           'It is not to be made to any creature, but to God alone: and '
           'that it may be accepted, it is to be made voluntarily, out of '
           'faith and conscience of duty, in way of thankfulness for mercy '
           'received, or for obtaining of what we want; whereby we more '
           'strictly bind ourselves to necessary duties, or to other things, '
           'so far and so long as they may fitly conduce thereunto.',
          7:
           'No man may vow to do any thing forbidden in the Word of God, '
           'or what would hinder any duty therein commanded, or which is not '
           'in his own power, and for the performance of which he hath no '
           'promise or ability from God. In which respects, monastical vows of '
           'perpetual single life, professed poverty, and regular obedience, '
           'are so far from being degrees of higher perfection, that they are '
           'superstitious and sinful snares, in which no Christian may '
           'entangle himself.'},
     23: {
          0:
           'Chapter 23. Of the Civil Magistrate',
          1:
           'God, the Supreme Lord and King of all the world, hath ordained '
           'civil magistrates to be under him over the people, for his own '
           'glory and the public good; and to this end, hath armed them with '
           'the power of the sword, for the defense and encouragement of them '
           'that are good, and for the punishment of evil-doers.',
          2:
           'It is lawful for Christians to accept and execute the office '
           'of a magistrate when called thereunto; in the managing whereof, as '
           'they ought especially to maintain piety, justice, and peace, '
           'according to the wholesome laws of each commonwealth, so, for that '
           'end, they may lawfully, now under the New Testament, wage war upon '
           'just and necessary occasions.',
          3:
           'The civil magistrate may not assume to himself the '
           'administration of the Word and sacraments, or the power of the '
           'keys of the kingdom of heaven: yet he hath authority, and it is '
           'his duty, to take order, that unity and peace be preserved in the '
           'Church, that the truth of God be kept pure and entire; that all '
           'blasphemies and heresies be suppressed; all corruptions and abuses '
           'in worship and discipline prevented or reformed; and all the '
           'ordinances of God duly settled, administered, and observed. For '
           'the better effecting whereof, he hath power to call synods, to be '
           'present at them, and to provide that whatsoever is transacted in '
           'them be according to the mind of God.',
          4:
           'It is the duty of the people to pray for magistrates, to honor '
           'their persons, to pay them tribute and other dues, to obey their '
           'lawful commands, and to be subject to their authority, for '
           "conscience' sake. Infidelity, or difference in religion, doth not "
           "make void the magistrate's just and legal authority, nor free the "
           'people from their obedience to him: from which ecclesiastical '
           'persons are not exempted; much less hath the Pope any power or '
           'jurisdiction over them in their dominions, or over any of their '
           'people; and least of all to deprive them of their dominions or '
           'lives, if he shall judge them to be heretics, or upon any other '
           'pretense whatsoever.'},
     24: {
          0:
           'Chapter 24. Of Marriage and Divorce',
          1:
           'Marriage is to be between one man and one woman: neither is it '
           'lawful for any man to have more than one wife, nor for any woman '
           'to have more than one husband at the same time.',
          2:
           'Marriage was ordained for the mutual help of husband and wife; '
           'for the increase of mankind with a legitimate issue, and of the '
           'Church with an holy seed; and for preventing of uncleanness.',
          3:
           'It is lawful for all sorts of people to marry who are able '
           'with judgment to give their consent. Yet it is the duty of '
           'Christians to marry only in the Lord. And, therefore, such as '
           'profess the true reformed religion should not marry with infidels, '
           'Papists, or other idolaters: neither should such as are godly be '
           'unequally yoked, by marrying with such as are notoriously wicked '
           'in their life, or maintain damnable heresies.',
          4:
           'Marriage ought not to be within the degrees of consanguinity '
           'or affinity forbidden in the Word; nor can such incestuous '
           'marriages ever be made lawful by any law of man, or consent of '
           'parties, so as those persons may live together, as man and wife. '
           "The man may not marry any of his wife's kindred nearer in blood "
           "than he may of his own, nor the woman of her husband's kindred "
           'nearer in blood than of her own.',
          5:
           'Adultery or fornication, committed after a contract, being '
           'detected before marriage, giveth just occasion to the innocent '
           'party to dissolve that contract. In the case of adultery after '
           'marriage, it is lawful for the innocent party to sue out a '
           'divorce, and after the divorce to marry another, as if the '
           'offending party were dead.',
          6:
           'Although the corruption of man be such as is apt to study '
           'arguments, unduly to put asunder those whom God hath joined '
           'together in marriage; yet nothing but adultery, or such willful '
           'desertion as can no way be remedied by the Church or civil '
           'magistrate, is cause sufficient of dissolving the bond of '
           'marriage; wherein a public and orderly course of proceeding is to '
           'be observed; and the persons concerned in it, not left to their '
           'own wills and discretion in their own case.'},
     25: {
          0:
           'Chapter 25. Of the Church',
          1:
           'The catholic or universal Church, which is invisible, consists '
           'of the whole number of the elect, that have been, are, or shall be '
           'gathered into one, under Christ the head thereof; and is the '
           'spouse, the body, the fullness of Him that filleth all in all.',
          2:
           'The visible Church, which is also catholic or universal under '
           'the Gospel (not confined to one nation, as before under the law), '
           'consists of all those throughout the world that profess the true '
           'religion; and of their children: and is the kingdom of the Lord '
           'Jesus Christ, the house and family of God, out of which there is '
           'no ordinary possibility of salvation.',
          3:
           'Unto this catholic and visible Church, Christ hath given the '
           'ministry, oracles, and ordinances of God, for the gathering and '
           'perfecting of the saints, in this life, to the end of the world; '
           'and doth by his own presence and Spirit, according to his promise, '
           'make them effectual thereunto.',
          4:
           'This catholic Church hath been sometimes more, sometimes less, '
           'visible. And particular Churches, which are members thereof, are '
           'more or less pure, according as the doctrine of the gospel is '
           'taught and embraced, ordinances administered, and public worship '
           'performed more or less purely in them.',
          5:
           'The purest Churches under heaven are subject both to mixture '
           'and error: and some have so degenerated as to become apparently no '
           'Churches of Christ. Nevertheless, there shall be always a Church '
           'on earth, to worship God according to his will.',
          6:
           'There is no other head of the Church but the Lord Jesus '
           'Christ: nor can the Pope of Rome in any sense be head thereof; but '
           'is that Antichrist, that man of sin and son of perdition, that '
           'exalteth himself in the Church against Christ, and all that is '
           'called God.'},
     26: {
          0:
           'Chapter 26. Of the Communion of the Saints',
          1:
           'All saints that are united to Jesus Christ their head, by his '
           'Spirit and by faith, have fellowship with him in his graces, '
           'sufferings, death, resurrection, and glory: and, being united to '
           "one another in love, they have communion in each other's gifts and "
           'graces, and are obliged to the performance of such duties, public '
           'and private, as to conduce to their mutual good, both in the '
           'inward and outward man.',
          2:
           'Saints by profession, are bound to maintain an holy fellowship '
           'and communion in the worship of God, and in performing such other '
           'spiritual services as tend to their mutual edification; as also in '
           'relieving each other in outward things, according to their several '
           'abilities and necessities. Which communion, as God offereth '
           'opportunity, is to be extended unto all those who, in every place, '
           'call upon the name of the Lord Jesus.',
          3:
           'This communion which the saints have with Christ, doth not '
           'make them in any wise partakers of the substance of the Godhead, '
           'or to be equal with Christ in any respect: either of which to '
           'affirm, is impious and blasphemous. Nor doth their communion one '
           'with another as saints, take away or infringe the title or '
           'property which each man hath in his goods and possessions.'},
     27: {
          0:
           'Chapter 27. Of the Sacraments',
          1:
           'Sacraments are holy signs and seals of the covenant of grace, '
           'immediately instituted by God, to represent Christ and his '
           'benefits, and to confirm our interest in him: as also to put a '
           'visible difference between those that belong unto the Church, and '
           'the rest of the world; and solemnly to engage them to the service '
           'of God in Christ, according to his Word.',
          2:
           'There is in every sacrament a spiritual relation, or '
           'sacramental union, between the sign and the thing signified; '
           'whence it comes to pass that the names and effects of the one are '
           'attributed to the other.',
          3:
           'The grace which is exhibited in or by the sacraments, rightly '
           'used, is not conferred by any power in them; neither doth the '
           'efficacy of a sacrament depend upon the piety or intention of him '
           'that doth administer it, but upon the work of the Spirit, and the '
           'word of institution, which contains, together with a precept '
           'authorizing the use thereof, a promise of benefit to worthy '
           'receivers.',
          4:
           'There be only two sacraments ordained by Christ our Lord in '
           'the gospels, that is to say, Baptism and the Supper of the Lord: '
           'neither or which may be dispensed by any but a minister of the '
           'Word, lawfully ordained.',
          5:
           'The sacraments of the Old Testament, in regard of the spiritual '
           'things thereby signified and exhibited, were, for substance, the '
           'same with those of the New.'},
     28: {
          0:
           'Chapter 28. Of Baptism',
          1:
           'Baptism is a sacrament of the New Testament, ordained by Jesus '
           'Christ, not only for the solemn admission of the party baptized '
           'into the visible Church, but also to be unto him a sign and seal '
           'of the covenant of grace, of his ingrafting into Christ, of '
           'regeneration, of remission of sins, and of his giving up unto God, '
           'through Jesus Christ, to walk in newness of life: which sacrament '
           "is, by Christ's own appointment, to be continued in his Church "
           'until the end of the world.',
          2:
           'The outward element to be used in the sacrament is water, '
           'wherewith the party is to be baptized in the name of the Father, '
           'and of the Son, and of the Holy Ghost, by a minister of the '
           'gospel, lawfully called thereunto.',
          3:
           'Dipping of the person into the water is not necessary; but '
           'baptism is rightly administered by pouring or sprinkling water '
           'upon the person.',
          4:
           'Not only those that do actually profess faith in and obedience '
           'unto Christ, but also the infants of one or both believing parents '
           'are to be baptized.',
          5:
           'Although it be a great sin to contemn or neglect this '
           'ordinance, yet grace and salvation are not so inseparably annexed '
           'unto it as that no person can be regenerated or saved without it, '
           'or that all that are baptized are undoubtedly regenerated.',
          6:
           'The efficacy of baptism is not tied to that moment of time '
           'wherein it is administered; yet, notwithstanding, by the right use '
           'of this ordinance, the grace promised is not only offered, but '
           'really exhibited and conferred by the Holy Ghost, to such (whether '
           'of age or infants) as that grace belongeth unto, according to the '
           "counsel of God's own will, in his appointed time.",
          7:
           'The sacrament of Baptism is but once to be administered to '
           'any person.'},
     29: {
          0:
           "Chapter 29. Of the Lord's Supper",
          1:
           'Our Lord Jesus, in the night wherein he was betrayed, '
           "instituted the sacrament of his body and blood, called the Lord's "
           'Supper, to be observed in his Church unto the end of the world; '
           'for the perpetual remembrance of the sacrifice of himself in his '
           'death, the sealing all benefits thereof unto true believers, their '
           'spiritual nourishment and growth in him, their further engagement '
           'in and to all duties which they owe unto him; and to be a bond and '
           'pledge of their communion with him, and with each other, as '
           'members of his mystical body.',
          2:
           'In this sacrament Christ is not offered up to his Father, nor '
           'any real sacrifice made at all for remission of sins of the quick '
           'or dead, but a commemoration of that one offering up of himself, '
           'by himself, upon the cross, once for all, and a spiritual oblation '
           'of all possible praise unto God for the same; so that the Popish '
           'sacrifice of the mass, as they call it, is most abominably '
           "injurious to Christ's one only sacrifice, the alone propitiation "
           'for all the sins of the elect.',
          3:
           'The Lord Jesus hath, in this ordinance, appointed his '
           'ministers to declare his word of institution to the people, to '
           'pray, and bless the elements of bread and wine, and thereby to set '
           'them apart from a common to an holy use; and to take and break the '
           'bread, to take the cup, and (they communicating also themselves) '
           'to give both to the communicants; but to none who are not then '
           'present in the congregation.',
          4:
           'Private masses, or receiving this sacrament by a priest, or '
           'any other, alone; as likewise the denial of the cup to the people; '
           'worshipping the elements, the lifting them up, or carrying them '
           'about for adoration, and the reserving them for any pretended '
           'religious use, are all contrary to the nature of this sacrament, '
           'and to the institution of Christ.',
          5:
           'The outward elements in this sacrament, duly set apart to the '
           'uses ordained by Christ, have such relation to him crucified, as '
           'that truly, yet sacramentally only, they are sometimes called by '
           'the name of the things they represent, to wit, the body and blood '
           'of Christ; albeit, in substance and nature, they still remain '
           'truly, and only, bread and wine, as they were before.',
          6:
           'That doctrine which maintains a change of the substance of '
           "bread and wine, into the substance of Christ's body and blood "
           '(commonly called transubstantiation) by consecration of a priest, '
           'or by any other way, is repugnant, not to Scripture alone, but '
           'even to common-sense and reason; overthroweth the nature of the '
           'sacrament; and hath been, and is, the cause of manifold '
           'superstitions, yea, of gross idolatries.',
          7:
           'Worthy receivers, outwardly partaking of the visible elements '
           'in this sacrament, do then also inwardly by faith, really and '
           'indeed, yet not carnally and corporally, but spiritually, receive '
           'and feed upon Christ crucified, and all benefits of his death: the '
           'body and blood of Christ being then not corporally or carnally in, '
           'with, or under the bread and wine; yet as really, but spiritually, '
           'present to the faith of believers in that ordinance, as the '
           'elements themselves are to their outward senses.',
          8:
           "Although ignorant and wicked men receive the outward elements "
           "in this sacrament; yet, they receive not the thing signified "
           "thereby; but, by their unworthy coming thereunto, are guilty of the "
           "body and blood of the Lord, to their own damnation. Wherefore, all "
           "ignorant and ungodly persons, as they are unfit to enjoy communion "
           "with Him, so are they unworthy of the Lord's table; and cannot, "
           "without great sin against Christ, while they remain such, partake "
           "of these holy mysteries, or be admitted thereunto."},
     30: {
          0:
           'Chapter 30. Of Church Censures',
          1:
           'The Lord Jesus, as king and head of his Church, hath therein '
           'appointed a government in the hand of Church officers, distinct '
           'from the civil magistrate.',
          2:
           'To these officers the keys of the Kingdom of Heaven are '
           'committed, by virtue whereof they have power respectively to '
           'retain and remit sins, to shut that kingdom against the '
           'impenitent, both by the word and censures; and to open it unto '
           'penitent sinners, by the ministry of the gospel, and by absolution '
           'from censures, as occasion shall require.',
          3:
           'Church censures are necessary for the reclaiming and gaining '
           'of offending brethren; for deterring of others from like offenses; '
           'for purging out of that leaven which might infect the whole lump; '
           'for vindicating the honor of Christ, and the holy profession of '
           'the gospel; and for preventing the wrath of God, which might '
           'justly fall upon the Church, if they should suffer his covenant, '
           'and the seals thereof, to be profaned by notorious and obstinate '
           'offenders.',
          4:
           'For the better attaining of these ends, the officers of the '
           'Church are to proceed by admonition, suspension from the sacrament '
           "of the Lord's Supper for a season, and by excommunication from the "
           'Church, according to the nature of the crime, and demerit of the '
           'person.'},
     31: {
          0:
           'Chapter 31. Of Synods and Councils',
          1:
           'For the better government and further edification of the '
           'Church, there ought to be such assemblies as are commonly called '
           'synods or councils.',
          2:
           'As magistrates may lawfully call a synod of ministers and '
           'other fit persons to consult and advise with about matters of '
           'religion; so, if magistrates be open enemies of the Church, the '
           'ministers of Christ, of themselves, by virtue of their office, or '
           'they, with other fit persons, upon delegation from their churches, '
           'may meet together in such assemblies.',
          3:
           'It belongeth to synods and councils, ministerially, to '
           'determine controversies of faith, and cases of conscience; to set '
           'down rules and directions for the better ordering of the public '
           'worship of God, and government of his Church; to receive '
           'complaints in cases of maladministration, and authoritatively to '
           'determine the same: which decrees and determinations, if consonant '
           'to the Word of God, are to be received with reverence and '
           'submission, not only for their agreement with the Word, but also '
           'for the power whereby they are made, as being an ordinance of God, '
           'appointed thereunto in his Word.',
          4:
           "All synods or councils since the apostles' times, whether "
           'general or particular, may err, and many have erred; therefore '
           'they are not to be made the rule of faith or practice, but to be '
           'used as a help in both.',
          5:
           'Synods and councils are to handle or conclude nothing but that '
           'which is ecclesiastical: and are not to intermeddle with civil '
           'affairs which concern the commonwealth, unless by way of humble '
           'petition in cases extraordinary; or by way of advice for '
           'satisfaction of conscience, if they be thereunto required by the '
           'civil magistrate.'},
     32: {
          0:
           'Chapter 32. Of the State of Man After Death, and of the '
           'Resurrection of the Dead',
          1:
           'The bodies of men, after death, return to dust, and see '
           'corruption; but their souls (which neither die nor sleep), having '
           'an immortal subsistence, immediately return to God who gave them. '
           'The souls of the righteous, being then made perfect in holiness, '
           'are received into the highest heavens, where they behold the face '
           'of God in light and glory, waiting for the full redemption of '
           'their bodies; and the souls of the wicked are cast into hell, '
           'where they remain in torments and utter darkness, reserved to the '
           'judgment of the great day. Besides these two places for souls '
           'separated from their bodies, the Scripture acknowledgeth none.',
          2:
           'At the last day, such as are found alive shall not die, but be '
           'changed: and all the dead shall be raised up with the self-same '
           'bodies, and none other, although with different qualities, which '
           'shall be united again to their souls forever.',
          3:
           'The bodies of the unjust shall, by the power of Christ, be '
           'raised to dishonor; the bodies of the just, by his Spirit, unto '
           'honor, and be made conformable to his own glorious body.'},
     33: {
          0:
           'Chapter 33. Of the Last Judgment.',
          1:
           'God hath appointed a day, wherein he will judge the world in '
           'righteousness by Jesus Christ, to whom all power and judgment is '
           'given of the Father. In which day, not only the apostate angels '
           'shall be judged; but likewise all persons, that have lived upon '
           'earth, shall appear before the tribunal of Christ, to give an '
           'account of their thoughts, words, and deeds; and to receive '
           'according to what they have done in the body, whether good or evil.',
          2:
           "The end of God's appointing this day, is for the manifestation "
           'of the glory of his mercy in the eternal salvation of the elect; '
           'and of his justice in the damnation of the reprobate, who are '
           'wicked and disobedient. For then shall the righteous go into '
           'everlasting life, and receive that fullness of joy and refreshing '
           'which shall come from the presence of the Lord: but the wicked, '
           'who know not God, and obey not the gospel of Jesus Christ, shall '
           'be cast into eternal torments, and punished with everlasting '
           'destruction from the presence of the Lord, and from the glory of '
           'his power.',
          3:
           'As Christ would have us to be certainly persuaded that there '
           'shall be a day of judgment, both to deter all men from sin, and '
           'for the greater consolation of the godly in their adversity: so '
           'will he have that day unknown to men, that they may shake off all '
           'carnal security, and be always watchful, because they know not at '
           'what hour the Lord will come; and may be ever prepared to say, '
           'Come, Lord Jesus, come quickly. Amen.'}
    }

    output = ''
    if first:
        output += doc[chap][0] + ". "
    for x in range(start, stop+1):
        output += "Paragraph " + str(x) + ", " + doc[chap][x]
        
    return output

def get_shorter_catechism(start, stop):
    doc = {
        1: ('What is the chief end of man?',
            "Man's chief end is to glorify God, and to enjoy him forever."),
        2: ('What rule hath God given to direct us how we may glorify and enjoy '
            'him?',
            'The Word of God, which is contained in the Scriptures of the Old and '
            'New Testaments, is the only rule to direct us how we may glorify and '
            'enjoy him.'),
        3: ('What do the Scriptures principally teach?',
            'The Scriptures principally teach what man is to believe concerning '
            'God, and what duty God requires of man.'),
        4: ('What is God?',
            'God is a spirit, infinite, eternal, and unchangeable, in his being, '
            'wisdom, power, holiness, justice, goodness and truth.'),
        5: ('Are there more Gods than one?',
            'There is but one only, the living and true God.'),
        6:
        ('How many persons are there in the godhead?',
         'There are three persons in the Godhead; the Father, the Son, and the '
         'Holy Ghost; and these three are one God, the same in substance, equal '
         'in power and glory.'),
        7: ('What are the decrees of God?',
            'The decrees of God are his eternal purpose, according to the counsel '
            'of his will, whereby, for his own glory, he hath foreordained '
            'whatsoever comes to pass.'),
        8: ('How doth God execute his decrees?',
            'God executeth his decrees in the works of creation and providence.'),
        9: ('What is the work of creation?',
            "The work of creation is God's making all things of nothing, by the "
            'word of his power, in the space of six days, and all very good.'),
        10: ('How did God create man?',
             'God created man male and female, after his own image, in knowledge, '
             'righteousness and holiness, with dominion over the creatures.'),
        11: ("What are God's works of providence?",
             "God's works of providence are his most holy, wise and powerful "
             'preserving and governing all his creatures, and all their actions.'),
        12:
        ('What special act of providence did God exercise toward man in the '
         'estate wherein he was created?',
         'When God had created man, he entered into a covenant of life with '
         'him, upon condition of perfect obedience; forbidding him to eat of '
         'the tree of the knowledge of good and evil, upon the pain of death.'),
        13:
        ('Did our first parents continue in the estate wherein they were '
         'created?',
         'Our first parents, being left to the freedom of their own will, fell '
         'from the estate wherein they were created, by sinning against God.'),
        14: ('What is sin?',
             'Sin is any want of conformity unto, or transgression of, the law of '
             'God.'),
        15: ('What was the sin whereby our first parents fell from the estate '
             'wherein they were created?',
             'The sin whereby our first parents fell from the estate wherein they '
             'were created was their eating the forbidden fruit.'),
        16: (
            "Did all mankind fall in Adam's first transgression?",
            'The covenant being made with Adam, not only for himself, but for his '
            'posterity; all mankind, descending from him by ordinary generation, '
            'sinned in him, and fell with him, in his first transgression.'),
        17: ('Into what estate did the fall bring mankind?',
             'The fall brought mankind into an estate of sin and misery.'),
        18: ('Wherein consists the sinfulness of that estate whereinto man fell?',
             'The sinfulness of that estate whereinto man fell consists in the '
             "guilt of Adam's first sin, the want of original righteousness, and "
             'the corruption of his whole nature, which is commonly called '
             'original sin; together with all actual transgressions which proceed '
             'from it.'),
        19: (
            'What is the misery of that estate whereinto man fell?',
            'All mankind by their fall lost communion with God, are under his '
            'wrath and curse, and so made liable to all miseries in this life, to '
            'death itself, and to the pains of hell forever.'),
        20: (
            'Did God leave all mankind to perish in the estate of sin and misery?',
            'God having, out of his mere good pleasure, from all eternity, '
            'elected some to everlasting life, did enter into a covenant of '
            'grace, to deliver them out of the estate of sin and misery, and to '
            'bring them into an estate of salvation by a redeemer.'),
        21:
        ("Who is the redeemer of God's elect?",
         "The only redeemer of God's elect is the Lord Jesus Christ, who, "
         'being the eternal Son of God, became man, and so was, and continueth '
         'to be, God and man in two distinct natures, and one person, forever.'),
        22: (
            'How did Christ, being the Son of God, become man?',
            'Christ, the Son of God, became man, by taking to himself a true body '
            'and a reasonable soul, being conceived by the power of the Holy '
            'Ghost in the womb of the virgin Mary, and born of her, yet without '
            'sin.'),
        23: ('What offices doth Christ execute as our redeemer?',
             'Christ, as our redeemer, executeth the offices of a prophet, of a '
             'priest, and of a king, both in his estate of humiliation and '
             'exaltation.'),
        24: (
            'How doth Christ execute the office of a prophet?',
            'Christ executeth the office of a prophet, in revealing to us, by his '
            'word and Spirit, the will of God for our salvation.'),
        25: ('How doth Christ execute the office of a priest?',
             'Christ executeth the office of a priest, in his once offering up of '
             'himself a sacrifice to satisfy divine justice, and reconcile us to '
             'God; and in making continual intercession for us.'),
        26: (
            'How doth Christ execute the office of a king?',
            'Christ executeth the office of a king, in subduing us to himself, in '
            'ruling and defending us, and in restraining and conquering all his '
            'and our enemies.'),
        27: (
            "Wherein did Christ's humiliation consist?",
            "Christ's humiliation consisted in his being born, and that in a low "
            'condition, made under the law, undergoing the miseries of this life, '
            'the wrath of God, and the cursed death of the cross; in being '
            'buried, and continuing under the power of death for a time.'),
        28: (
            "Wherein consisteth Christ's exaltation?",
            "Christ's exaltation consisteth in his rising again from the dead on "
            'the third day, in ascending up into heaven, in sitting at the right '
            'hand of God the Father, and in coming to judge the world at the last '
            'day.'),
        29: ('How are we made partakers of the redemption purchased by Christ?',
             'We are made partakers of the redemption purchased by Christ, by the '
             'effectual application of it to us by his Holy Spirit.'),
        30: ('How doth the Spirit apply to us the redemption purchased by Christ?',
             'The Spirit applieth to us the redemption purchased by Christ, by '
             'working faith in us, and thereby uniting us to Christ in our '
             'effectual calling.'),
        31: (
            'What is effectual calling?',
            "Effectual calling is the work of God's Spirit, whereby, convincing "
            'us of our sin and misery, enlightening our minds in the knowledge of '
            'Christ, and renewing our wills, he doth persuade and enable us to '
            'embrace Jesus Christ, freely offered to us in the gospel.'),
        32: (
            'What benefits do they that are effectually called partake of in this '
            'life?', 'They that are effectually called do in this life partake of '
            'justification, adoption and sanctification, and the several benefits '
            'which in this life do either accompany or flow from them.'),
        33: ('What is justification?',
             "Justification is an act of God's free grace, wherein he pardoneth "
             'all our sins, and accepteth us as righteous in his sight, only for '
             'the righteousness of Christ imputed to us, and received by faith '
             'alone.'),
        34: (
            'What is adoption?',
            "Adoption is an act of God's free grace, whereby we are received into "
            'the number, and have a right to all the privileges of, the sons of '
            'God.'),
        35: ('What is sanctification?',
             "Sanctification is the work of God's free grace, whereby we are "
             'renewed in the whole man after the image of God, and are enabled '
             'more and more to die unto sin, and live unto righteousness.'),
        36: (
            'What are the benefits which in this life do accompany or flow from '
            'justification, adoption and sanctification?',
            'The benefits which in this life do accompany or flow from '
            "justification, adoption and sanctification, are, assurance of God's "
            'love, peace of conscience, joy in the Holy Ghost, increase of grace, '
            'and perseverance therein to the end.'),
        37: ('What benefits do believers receive from Christ at death?',
             'The souls of believers are at their death made perfect in holiness, '
             'and do immediately pass into glory; and their bodies, being still '
             'united to Christ, do rest in their graves till the resurrection.'),
        38: ('What benefits do believers receive from Christ at the resurrection?',
             'At the resurrection, believers being raised up in glory, shall be '
             'openly acknowledged and acquitted in the day of judgment, and made '
             'perfectly blessed in the full enjoying of God to all eternity.'),
        39: ('What is the duty which God requireth of man?',
             'The duty which God requireth of man is obedience to his revealed '
             'will.'),
        40: ('What did God at first reveal to man for the rule of his obedience?',
             'The rule which God at first revealed to man for his obedience was '
             'the moral law.'),
        41: ('Where is the moral law summarily comprehended?',
             'The moral law is summarily comprehended in the ten commandments.'),
        42: (
            'What is the sum of the ten commandments?',
            'The sum of the ten commandments is to love the Lord our God with all '
            'our heart, with all our soul, with all our strength, and with all '
            'our mind; and our neighbor as ourselves.'),
        43: (
            'What is the preface to the ten commandments?',
            'The preface to the ten commandments is in these words, I am the Lord '
            'thy God, which have brought thee out of the land of Egypt, out of '
            'the house of bondage.'),
        44: ('What doth the preface to the ten commandments teach us?',
             'The preface to the ten commandments teacheth us that because God is '
             'the Lord, and our God, and redeemer, therefore we are bound to keep '
             'all his commandments.'),
        45: ('Which is the first commandment?',
             'The first commandment is, Thou shalt have no other gods before me.'),
        46: (
            'What is required in the first commandment?',
            'The first commandment requireth us to know and acknowledge God to be '
            'the only true God, and our God; and to worship and glorify him '
            'accordingly.'),
        47: ('What is forbidden in the first commandment?',
             'The first commandment forbiddeth the denying, or not worshiping and '
             'glorifying the true God as God, and our God; and the giving of that '
             'worship and glory to any other, which is due to him alone.'),
        48: (
            'What are we specially taught by these words before me in the first '
            'commandment?',
            'These words before me in the first commandment teach us that God, '
            'who seeth all things, taketh notice of, and is much displeased with, '
            'the sin of having any other god.'),
        49: ('Which is the second commandment?',
             'The second commandment is, Thou shalt not make unto thee any graven '
             'image, or any likeness of anything that is in heaven above, or that '
             'is in the earth beneath, or that is in the water under the earth: '
             'thou shalt not bow down thyself to them, nor serve them: for I the '
             'Lord thy God am a jealous God, visiting the iniquity of the fathers '
             'upon the children unto the third and fourth generation of them that '
             'hate me; and showing mercy unto thousands of them that love me, and '
             'keep my commandments.'),
        50: ('What is required in the second commandment?',
             'The second commandment requireth the receiving, observing, and '
             'keeping pure and entire, all such religious worship and ordinances '
             'as God hath appointed in his word.'),
        51: ('What is forbidden in the second commandment?',
             'The second commandment forbiddeth the worshiping of God by images, '
             'or any other way not appointed in his word.'),
        52: (
            'What are the reasons annexed to the second commandment?',
            "The reasons annexed to the second commandment are, God's sovereignty "
            'over us, his propriety in us, and the zeal he hath to his own '
            'worship.'),
        53: ('Which is the third commandment?',
             'The third commandment is, Thou shalt not take the name of the Lord '
             'thy God in vain: for the Lord will not hold him guiltless that '
             'taketh his name in vain.'),
        54: ('What is required in the third commandment?',
             "The third commandment requireth the holy and reverent use of God's "
             'names, titles, attributes, ordinances, word and works.'),
        55: ('What is forbidden in the third commandment?',
             'The third commandment forbiddeth all profaning or abusing of '
             'anything whereby God maketh himself known.'),
        56: (
            'What is the reason annexed to the third commandment?',
            'The reason annexed to the third commandment is that however the '
            'breakers of this commandment may escape punishment from men, yet the '
            'Lord our God will not suffer them to escape his righteous judgment.'),
        57:
        ('Which is the fourth commandment?',
         'The fourth commandment is, Remember the sabbath day, to keep it holy'),
        58: ('What is required in the fourth commandment?',
             'The fourth commandment requireth the keeping holy to God such set '
             'times as he hath appointed in his word; expressly one whole day in '
             'seven, to be a holy sabbath to himself.'),
        59: ('Which day of the seven hath God appointed to be the weekly sabbath?',
             'From the beginning of the world to the resurrection of Christ, God '
             'appointed the seventh day of the week to be the weekly sabbath; and '
             'the first day of the week ever since, to continue to the end of the '
             'world, which is the Christian sabbath.'),
        60: (
            'How is the sabbath to be sanctified?',
            'The sabbath is to be sanctified by a holy resting all that day, even '
            'from such worldly employments and recreations as are lawful on other '
            'days; and spending the whole time in the public and private '
            "exercises of God's worship, except so much as is to be taken up in "
            'the works of necessity and mercy.'),
        61: (
            'What is forbidden in the fourth commandment?',
            'The fourth commandment forbiddeth the omission or careless '
            'performance of the duties required, and the profaning the day by '
            'idleness, or doing that which is in itself sinful, or by unnecessary '
            'thoughts, words or works, about our worldly employments or '
            'recreations.'),
        62: (
            'What are the reasons annexed to the fourth commandment?',
            "The reasons annexed to the fourth commandment are, God's allowing us "
            'six days of the week for our own employments, his challenging a '
            'special propriety in the seventh, his own example, and his blessing '
            'the sabbath day.'),
        63: ('Which is the fifth commandment?',
             'The fifth commandment is, Honor thy father and thy mother; that thy '
             'days may be long upon the land which the Lord thy God giveth thee.'),
        64: ('What is required in the fifth commandment?',
             'The fifth commandment requireth the preserving the honor, and '
             'performing the duties, belonging to every one in their several '
             'places and relations, as superiors, inferiors or equals.'),
        65: (
            'What is forbidden in the fifth commandment?',
            'The fifth commandment forbiddeth the neglecting of, or doing '
            'anything against, the honor and duty which belongeth to every one in '
            'their several places and relations.'),
        66: ('What is the reason annexed to the fifth commandment?',
             'The reason annexed to the fifth commandment is a promise of long '
             "life and prosperity (as far as it shall serve for God's glory and "
             'their own good) to all such as keep this commandment.'),
        67: ('Which is the sixth commandment?',
             'The sixth commandment is, Thou shalt not kill.'),
        68: (
            'What is required in the sixth commandment?',
            'The sixth commandment requireth all lawful endeavors to preserve our '
            'own life, and the life of others.'),
        69: (
            'What is forbidden in the sixth commandment?',
            'The sixth commandment forbiddeth the taking away of our own life, or '
            'the life of our neighbor unjustly, or whatsoever tendeth thereunto.'),
        70: ('Which is the seventh commandment?',
             'The seventh commandment is, Thou shalt not commit adultery.'),
        71: ('What is required in the seventh commandment?',
             'The seventh commandment requireth the preservation of our own and '
             "our neighbor's chastity, in heart, speech and behavior."),
        72: ('What is forbidden in the seventh commandment?',
             'The seventh commandment forbiddeth all unchaste thoughts, words and '
             'actions.'),
        73: ('Which is the eighth commandment?',
             'The eighth commandment is, Thou shalt not steal.'),
        74: (
            'What is required in the eighth commandment?',
            'The eighth commandment requireth the lawful procuring and furthering '
            'the wealth and outward estate of ourselves and others.'),
        75: ('What is forbidden in the eighth commandment?',
             'The eighth commandment forbiddeth whatsoever doth or may unjustly '
             "hinder our own or our neighbor's wealth or outward estate."),
        76: ('Which is the ninth commandment?',
             'The ninth commandment is, Thou shalt not bear false witness against '
             'thy neighbor.'),
        77: ('What is required in the ninth commandment?',
             'The ninth commandment requireth the maintaining and promoting of '
             "truth between man and man, and of our own and our neighbor's good "
             'name, especially in witness-bearing.'),
        78: (
            'What is forbidden in the ninth commandment?',
            'The ninth commandment forbiddeth whatsoever is prejudicial to truth, '
            "or injurious to our own or our neighbor's good name."),
        79: (
            'Which is the tenth commandment?',
            "The tenth commandment is, Thou shalt not covet thy neighbor's house, "
            "thou shalt not covet thy neighbor's wife, nor his manservant, nor "
            'his maidservant, nor his ox, nor his ass, nor anything that is thy '
            "neighbor's."),
        80: ('What is required in the tenth commandment?',
             'The tenth commandment requireth full contentment with our own '
             'condition, with a right and charitable frame of spirit toward our '
             'neighbor, and all that is his.'),
        81: ('What is forbidden in the tenth commandment?',
             'The tenth commandment forbiddeth all discontentment with our own '
             'estate, envying or grieving at the good of our neighbor, and all '
             'inordinate motions and affections to anything that is his.'),
        82: ('Is any man able perfectly to keep the commandments of God?',
             'No mere man since the fall is able in this life perfectly to keep '
             'the commandments of God, but doth daily break them in thought, word '
             'and deed.'),
        83: ('Are all transgressions of the law equally heinous?',
             'Some sins in themselves, and by reason of several aggravations, are '
             'more heinous in the sight of God than others.'),
        84: ('What doth every sin deserve?',
             "Every sin deserveth God's wrath and curse, both in this life, and "
             'that which is to come.'),
        85: ('What doth God require of us that we may escape his wrath and curse '
             'due to us for sin?',
             'To escape the wrath and curse of God due to us for sin, God '
             'requireth of us faith in Jesus Christ, repentance unto life, with '
             'the diligent use of all the outward means whereby Christ '
             'communicateth to us the benefits of redemption.'),
        86: (
            'What is faith in Jesus Christ?',
            'Faith in Jesus Christ is a saving grace, whereby we receive and rest '
            'upon him alone for salvation, as he is offered to us in the gospel.'),
        87: ('What is repentance unto life?',
             'Repentance unto life is a saving grace, whereby a sinner, out of a '
             'true sense of his sin, and apprehension of the mercy of God in '
             'Christ, doth, with grief and hatred of his sin, turn from it unto '
             'God, with full purpose of, and endeavor after, new obedience.'),
        88: (
            'What are the outward and ordinary means whereby Christ communicateth '
            'to us the benefits of redemption?',
            'The outward and ordinary means whereby Christ communicateth to us '
            'the benefits of redemption, are his ordinances, especially the word, '
            'sacraments, and prayer; all which are made effectual to the elect '
            'for salvation.'),
        89: ('How is the word made effectual to salvation?',
             'The Spirit of God maketh the reading, but especially the preaching, '
             'of the word, an effectual means of convincing and converting '
             'sinners, and of building them up in holiness and comfort, through '
             'faith, unto salvation.'),
        90: ('How is the word to be read and heard, that it may become effectual '
             'to salvation?',
             'That the word may become effectual to salvation, we must attend '
             'thereunto with diligence, preparation and prayer; receive it with '
             'faith and love, lay it up in our hearts, and practice it in our '
             'lives.'),
        91: (
            'How do the sacraments become effectual means of salvation?',
            'The sacraments become effectual means of salvation, not from any '
            'virtue in them, or in him that doth administer them; but only by the '
            'blessing of Christ, and the working of his Spirit in them that by '
            'faith receive them.'),
        92: ('What is a sacrament?',
             'A sacrament is an holy ordinance instituted by Christ; wherein, by '
             'sensible signs, Christ, and the benefits of the new covenant, are '
             'represented, sealed, and applied to believers.'),
        93: ('Which are the sacraments of the New Testament?',
             "The sacraments of the New Testament are baptism and the Lord's "
             'supper.'),
        94: ('What is baptism?',
             'Baptism is a sacrament, wherein the washing with water in the name '
             'of the Father, and of the Son, and of the Holy Ghost, doth signify '
             'and seal our ingrafting into Christ, and partaking of the benefits '
             "of the covenant of grace, and our engagement to be the Lord's."),
        95: (
            'To whom is baptism to be administered?',
            'Baptism is not to be administered to any that are out of the visible '
            'church, till they profess their faith in Christ, and obedience to '
            'him; but the infants of such as are members of the visible church '
            'are to be baptized.'),
        96: (
            "What is the Lord's supper?",
            "The Lord's supper is a sacrament, wherein, by giving and receiving "
            "bread and wine according to Christ's appointment, his death is "
            'showed forth; and the worthy receivers are, not after a corporal and '
            'carnal manner, but by faith, made partakers of his body and blood, '
            'with all his benefits, to their spiritual nourishment and growth in '
            'grace.'),
        97: ("What is required to the worthy receiving of the Lord's supper?",
             "It is required of them that would worthily partake of the Lord's "
             'supper, that they examine themselves of their knowledge to discern '
             "the Lord's body, of their faith to feed upon him, of their "
             'repentance, love, and new obedience; lest, coming unworthily, they '
             'eat and drink judgment to themselves.'),
        98: (
            'What is prayer?',
            'Prayer is an offering up of our desires unto God, for things '
            'agreeable to his will, in the name of Christ, with confession of our '
            'sins, and thankful acknowledgment of his mercies.'),
        99: (
            'What rule hath God given for our direction in prayer?',
            'The whole word of God is of use to direct us in prayer; but the '
            'special rule of direction is that form of prayer which Christ taught '
            "his disciples, commonly called the Lord's prayer."),
        100: (
            "What doth the preface of the Lord's prayer teach us?",
            "The preface of the Lord's prayer, which is, Our Father which art in "
            'heaven, teacheth us to draw near to God with all holy reverence and '
            'confidence, as children to a father able and ready to help us; and '
            'that we should pray with and for others.'),
        101: (
            'What do we pray for in the first petition?',
            'In the first petition, which is, Hallowed be thy name, we pray that '
            'God would enable us and others to glorify him in all that whereby '
            'he maketh himself known; and that he would dispose all things to '
            'his own glory.'),
        102: (
            'What do we pray for in the second petition?',
            'In the second petition, which is, Thy kingdom come, we pray that '
            "Satan's kingdom may be destroyed; and that the kingdom of grace may "
            'be advanced, ourselves and others brought into it, and kept in it; '
            'and that the kingdom of glory may be hastened.'),
        103: ('What do we pray for in the third petition?',
              'In the third petition, which is, Thy will be done in earth, as it '
              'is in heaven, we pray that God, by his grace, would make us able '
              'and willing to know, obey and submit to his will in all things, as '
              'the angels do in heaven.'),
        104: (
            'What do we pray for in the fourth petition?',
            'In the fourth petition, which is, Give us this day our daily bread, '
            "we pray that of God's free gift we may receive a competent portion "
            'of the good things of this life, and enjoy his blessing with them.'),
        105: ('What do we pray for in the fifth petition?',
              'In the fifth petition, which is, And forgive us our debts, as we '
              "forgive our debtors, we pray that God, for Christ's sake, would "
              'freely pardon all our sins; which we are the rather encouraged to '
              'ask, because by his grace we are enabled from the heart to forgive '
              'others.'),
        106: ('What do we pray for in the sixth petition?',
              'In the sixth petition, which is, And lead us not into temptation, '
              'but deliver us from evil, we pray that God would either keep us '
              'from being tempted to sin, or support and deliver us when we are '
              'tempted.'),
        107: ("What doth the conclusion of the Lord's prayer teach us?",
              "The conclusion of the Lord's prayer, which is, For thine is the "
              'kingdom, and the power, and the glory, forever, Amen, teacheth us '
              'to take our encouragement in prayer from God only, and in our '
              'prayers to praise him, ascribing kingdom, power and glory to him')
    }
    output = ''
    for x in range(start, stop+1):
        output += "Question " + str(x) + ". "
        output += doc[x][0]
        output += doc[x][1]
    return output


def get_larger_catechism(start, stop):
    doc = {
        1:
        ('What is the chief and highest end of man?',
         "Man's chief and highest end is to glorify God, and fully to enjoy him "
         'forever.'),
        2:
        ('How doth it appear that there is a God?',
         'The very light of nature in man, and the works of God, declare '
         'plainly that there is a God; but his word and Spirit only do '
         'sufficiently and effectually reveal him unto men for their salvation.'),
        3:
        ('What is the Word of God?',
         'The Holy Scriptures of the Old and New Testament are the Word of God, '
         'the only rule of faith and obedience.'),
        4:
        ('How doth it appear that the Scriptures are the Word of God?',
         'The Scriptures manifest themselves to be the Word of God, by their '
         'majesty and purity; by the consent of all the parts, and the scope of '
         'the whole, which is to give all glory to God; by their light and '
         'power to convince and convert sinners, to comfort and build up '
         'believers unto salvation: but the Spirit of God bearing witness by '
         'and with the Scriptures in the heart of man, is alone able fully to '
         'persuade it that they are the very Word of God.'),
        5: ('What do the Scriptures principally teach?',
            'The Scriptures principally teach what man is to believe concerning '
            'God, and what duty God requires of man.'),
        6: ('What do the Scriptures make known of God?',
            'The Scriptures make known what God is, the persons in the Godhead, '
            'his decrees, and the execution of his decrees.'),
        7: ('What is God?',
            'God is a Spirit, in and of himself infinite in being, glory, '
            'blessedness, and perfection; all-sufficient, eternal, unchangeable, '
            'incomprehensible, everywhere present, almighty, knowing all things, '
            'most wise, most holy, most just, most merciful and gracious, '
            'longsuffering, and abundant in goodness and truth.'),
        8: ('Are there more Gods than one?',
            'There is but one only, the living and true God.'),
        9: ('How many persons are there in the Godhead?',
            'There be three persons in the Godhead, the Father, the Son, and the '
            'Holy Ghost; and these three are one true, eternal God, the same in '
            'substance, equal in power and glory; although distinguished by their '
            'personal properties.'),
        10:
        ('What are the personal properties of the three persons in the Godhead?',
         'It is proper to the Father to beget the Son, and to the Son to be '
         'begotten of the Father, and to the Holy Ghost to proceed from the '
         'Father and the Son from all eternity.'),
        11: ('How doth it appear that the Son and the Holy Ghost are God equal '
             'with the Father?',
             'The Scriptures manifest that the Son and the Holy Ghost are God '
             'equal with the Father, ascribing unto them such names, attributes, '
             'works, and worship, as are proper to God only.'),
        12: ('What are the decrees of God?',
             "God's decrees are the wise, free, and holy acts of the counsel of "
             'his will, whereby, from all eternity, he hath, for his own glory, '
             'unchangeably foreordained whatsoever comes to pass in time, '
             'especially concerning angels and men.'),
        13:
        ('What hath God especially decreed concerning angels and men?',
         'God, by an eternal and immutable decree, out of his mere love, for '
         'the praise of his glorious grace, to be manifested in due time, hath '
         'elected some angels to glory; and in Christ hath chosen some men to '
         'eternal life, and the means thereof: and also, according to his '
         'sovereign power, and the unsearchable counsel of his own will '
         '(whereby he extendeth or withholdeth favor as he pleaseth), hath '
         'passed by and foreordained the rest to dishonor and wrath, to be for '
         'their sin inflicted, to the praise of the glory of his justice.'),
        14: ('How doth God execute his decrees?',
             'God executeth his decrees in the works of creation and providence, '
             'according to his infallible foreknowledge, and the free and '
             'immutable counsel of his own will.'),
        15: ('What is the work of creation?',
             'The work of creation is that wherein God did in the beginning, by '
             'the word of his power, make of nothing the world, and all things '
             'therein, for himself, within the space of six days, and all very '
             'good.'),
        16: ('How did God create angels?',
             'God created all the angels spirits, immortal, holy, excelling in '
             'knowledge, mighty in power, to execute his commandments, and to '
             'praise his name, yet subject to change.'),
        17: ('How did God create man?',
             'After God had made all other creatures, he created man male and '
             'female; formed the body of the man of the dust of the ground, and '
             'the woman of the rib of the man, endued them with living, '
             'reasonable, and immortal souls; made them after his own image, in '
             'knowledge, righteousness, and holiness; having the law of God '
             'written in their hearts, and power to fulfill it, and dominion over '
             'the creatures; yet subject to fall.'),
        18: ("What are God's works of providence?",
             "God's works of providence are his most holy, wise, and powerful "
             'preserving and governing all his creatures; ordering them, and all '
             'their actions, to his own glory.'),
        19:
        ("What is God's providence towards the angels?",
         'God by his providence permitted some of the angels, willfully and '
         'irrecoverably, to fall into sin and damnation, limiting and ordering '
         'that, and all their sins, to his own glory; and established the rest '
         'in holiness and happiness; employing them all, at his pleasure, in '
         'the administrations of his power, mercy, and justice.'),
        20:
        ('What was the providence of God toward man in the estate in which he '
         'was created?',
         'The providence of God toward man in the estate in which he was '
         'created, was the placing him in paradise, appointing him to dress '
         'it, giving him liberty to eat of the fruit of the earth; putting the '
         'creatures under his dominion, and ordaining marriage for his help; '
         'affording him communion with himself; instituting the Sabbath; '
         'entering into a covenant of life with him, upon condition of '
         'personal, perfect, and perpetual obedience, of which the tree of '
         'life was a pledge; and forbidding to eat of the tree of the '
         'knowledge of good and evil, upon the pain of death.'),
        21:
        ('Did man continue in that estate wherein God at first created him?',
         'Our first parents being left to the freedom of their own will, '
         'through the temptation of Satan, transgressed the commandment of God '
         'in eating the forbidden fruit; and thereby fell from the estate of '
         'innocency wherein they were created.'),
        22:
        ('Did all mankind fall in that first transgression?',
         'The covenant being made with Adam as a public person, not for '
         'himself only, but for his posterity, all mankind descending from him '
         'by ordinary generation, sinned in him, and fell with him in that '
         'first transgression.'),
        23: ('Into what estate did the fall bring mankind?',
             'The fall brought mankind into an estate of sin and misery.'),
        24: ('What is sin?',
             'Sin is any want of conformity unto, or transgression of, any law of '
             'God, given as a rule to the reasonable creature.'),
        25:
        ('Wherein consisteth the sinfulness of that estate whereinto man fell?',
         'The sinfulness of that estate whereinto man fell, consisteth in the '
         "guilt of Adam's first sin, the want of that righteousness wherein he "
         'was created, and the corruption of his nature, whereby he is utterly '
         'indisposed, disabled, and made opposite unto all that is spiritually '
         'good, and wholly inclined to all evil, and that continually; which '
         'is commonly called original sin, and from which do proceed all '
         'actual transgressions.'),
        26:
        ('How is original sin conveyed from our first parents unto their '
         'posterity?',
         'Original sin is conveyed from our first parents unto their posterity '
         'by natural generation, so as all that proceed from them in that way '
         'are conceived and born in sin.'),
        27: ('What misery did the fall bring upon mankind?',
             'The fall brought upon mankind the loss of communion with God, his '
             'displeasure and curse; so as we are by nature children of wrath, '
             'bond slaves to Satan, and justly liable to all punishments in this '
             'world, and that which is to come.'),
        28:
        ('What are the punishments of sin in this world?',
         'The punishments of sin in this world are either inward, as blindness '
         'of mind, a reprobate sense, strong delusions, hardness of heart, '
         'horror of conscience, and vile affections; or outward, as the curse '
         'of God upon the creatures for our sakes, and all other evils that '
         'befall us in our bodies, names, estates, relations, and employments; '
         'together with death itself.'),
        29: ('What are the punishments of sin in the world to come?',
             'The punishments of sin in the world to come, are everlasting '
             'separation from the comfortable presence of God, and most grievous '
             'torments in soul and body, without intermission, in hell-fire '
             'forever.'),
        30:
        ('Doth God leave all mankind to perish in the estate of sin and misery?',
         'God doth not leave all men to perish in the estate of sin and '
         'misery, into which they fell by the breach of the first covenant, '
         'commonly called the covenant of works; but of his mere love and '
         'mercy delivereth his elect out of it, and bringeth them into an '
         'estate of salvation by the second covenant, commonly called the '
         'covenant of grace.'),
        31: ('With whom was the covenant of grace made?',
             'The covenant of grace was made with Christ as the second Adam, and '
             'in him with all the elect as his seed.'),
        32:
        ('How is the grace of God manifested in the second covenant?',
         'The grace of God is manifested in the second covenant, in that he '
         'freely provideth and offereth to sinners a mediator, and life and '
         'salvation by him; and requiring faith as the condition to interest '
         'them in him, promiseth and giveth his Holy Spirit to all his elect, '
         'to work in them that faith, with all other saving graces; and to '
         'enable them unto all holy obedience, as the evidence of the truth of '
         'their faith and thankfulness to God, and as the way which he hath '
         'appointed them to salvation.'),
        33:
        ('Was the covenant of grace always administered after one and the same '
         'manner?',
         'The covenant of grace was not always administered after the same '
         'manner, but the administrations of it under the Old Testament were '
         'different from those under the New.'),
        34:
        ('How was the covenant of grace administered under the Old Testament?',
         'The covenant of grace was administered under the Old Testament, by '
         'promises, prophecies, sacrifices, circumcision, the passover, and '
         'other types and ordinances, which did all foresignify Christ then to '
         'come, and were for that time sufficient to build up the elect in '
         'faith in the promised messiah, by whom they then had full remission '
         'of sin, and eternal salvation.'),
        35:
        ('How is the covenant of grace administered under the New Testament?',
         'Under the New Testament, when Christ the substance was exhibited, '
         'the same covenant of grace was and still is to be administered in '
         'the preaching of the word, and the administration of the sacraments '
         "of baptism and the Lord's supper; in which grace and salvation are "
         'held forth in more fullness, evidence, and efficacy, to all nations.'),
        36:
        ('Who is the mediator of the covenant of grace?',
         'The only mediator of the covenant of grace is the Lord Jesus Christ, '
         'who, being the eternal Son of God, of one substance and equal with '
         'the Father, in the fullness of time became man, and so was and '
         'continues to be God and man, in two entire distinct natures, and one '
         'person, forever.'),
        37: ('How did Christ, being the Son of God, become man?',
             'Christ the Son of God became man, by taking to himself a true body, '
             'and a reasonable soul, being conceived by the power of the Holy '
             'Ghost in the womb of the virgin Mary, of her substance, and born of '
             'her, yet without sin.'),
        38: (
            'Why was it requisite that the mediator should be God?',
            'It was requisite that the mediator should be God, that he might '
            'sustain and keep the human nature from sinking under the infinite '
            'wrath of God, and the power of death; give worth and efficacy to his '
            "sufferings, obedience, and intercession; and to satisfy God's "
            'justice, procure his favor, purchase a peculiar people, give his '
            'Spirit to them, conquer all their enemies, and bring them to '
            'everlasting salvation.'),
        39: ('Why was it requisite that the mediator should be man?',
             'It was requisite that the mediator should be man, that he might '
             'advance our nature, perform obedience to the law, suffer and make '
             'intercession for us in our nature, have a fellow-feeling of our '
             'infirmities; that we might receive the adoption of sons, and have '
             'comfort and access with boldness unto the throne of grace.'),
        40: ('Why was it requisite that the mediator should be God and man in one '
             'person?',
             'It was requisite that the mediator, who was to reconcile God and '
             'man, should himself be both God and man, and this in one person, '
             'that the proper works of each nature might be accepted of God for '
             'us, and relied on by us, as the works of the whole person.'),
        41: ('Why was our mediator called Jesus?',
             'Our mediator was called Jesus, because he saveth his people from '
             'their sins.'),
        42: (
            'Why was our mediator called Christ?',
            'Our mediator was called Christ, because he was anointed with the '
            'Holy Ghost above measure; and so set apart, and fully furnished with '
            'all authority and ability, to execute the offices of prophet, '
            'priest, and king of his church, in the estate both of his '
            'humiliation and exaltation.'),
        43: ('How doth Christ execute the office of a prophet?',
             'Christ executeth the office of a prophet, in his revealing to the '
             'church, in all ages, by his Spirit and word, in divers ways of '
             'administration, the whole will of God, in all things concerning '
             'their edification and salvation.'),
        44: ('How doth Christ execute the office of a priest?',
             'Christ executeth the office of a priest, in his once offering '
             'himself a sacrifice without spot to God, to be a reconciliation for '
             'the sins of the people; and in making continual intercession for '
             'them.'),
        45: (
            'How doth Christ execute the office of a king?',
            'Christ executeth the office of a king, in calling out of the world a '
            'people to himself, and giving them officers, laws, and censures, by '
            'which he visibly governs them; in bestowing saving grace upon his '
            'elect, rewarding their obedience, and correcting them for their '
            'sins, preserving and supporting them under all their temptations and '
            'sufferings, restraining and overcoming all their enemies, and '
            'powerfully ordering all things for his own glory, and their good; '
            'and also in taking vengeance on the rest, who know not God, and obey '
            'not the gospel.'),
        46: ("What was the estate of Christ's humiliation?",
             "The estate of Christ's humiliation was that low condition, wherein "
             'he for our sakes, emptying himself of his glory, took upon him the '
             'form of a servant, in his conception and birth, life, death, and '
             'after his death, until his resurrection.'),
        47: (
            'How did Christ humble himself in his conception and birth?',
            'Christ humbled himself in his conception and birth, in that, being '
            'from all eternity the Son of God, in the bosom of the Father, he was '
            'pleased in the fullness of time to become the son of man, made of a '
            'woman of low estate, and to be born of her; with divers '
            'circumstances of more than ordinary abasement.'),
        48: ('How did Christ humble himself in his life?',
             'Christ humbled himself in his life, by subjecting himself to the '
             'law, which he perfectly fulfilled; and by conflicting with the '
             'indignities of the world, temptations of Satan, and infirmities in '
             'his flesh, whether common to the nature of man, or particularly '
             'accompanying that his low condition.'),
        49: (
            'How did Christ humble himself in his death?',
            'Christ humbled himself in his death, in that having been betrayed by '
            'Judas, forsaken by his disciples, scorned and rejected by the world, '
            'condemned by Pilate, and tormented by his persecutors; having also '
            'conflicted with the terrors of death, and the powers of darkness, '
            "felt and borne the weight of God's wrath, he laid down his life an "
            'offering for sin, enduring the painful, shameful, and cursed death '
            'of the cross.'),
        50: ("Wherein consisted Christ's humiliation after his death?",
             "Christ's humiliation after his death consisted in his being buried, "
             'and continuing in the state of the dead, and under the power of '
             'death till the third day; which hath been otherwise expressed in '
             'these words, He descended into hell.'),
        51: ("What was the estate of Christ's exaltation?",
             "The estate of Christ's exaltation comprehendeth his resurrection, "
             'ascension, sitting at the right hand of the Father, and his coming '
             'again to judge the world.'),
        52: ('How was Christ exalted in his resurrection?',
             'Christ was exalted in his resurrection, in that, not having seen '
             'corruption in death (of which it was not possible for him to be '
             'held), and having the very same body in which he suffered, with the '
             'essential properties thereof (but without mortality, and other '
             'common infirmities belonging to this life), really united to his '
             'soul, he rose again from the dead the third day by his own power; '
             'whereby he declared himself to be the Son of God, to have satisfied '
             'divine justice, to have vanquished death, and him that had power of '
             'it, and to be Lord of quick and dead: all which he did as a public '
             'person, the head of his church, for their justification, quickening '
             'in grace, support against enemies, and to assure them of their '
             'resurrection from the dead at the last day.'),
        53: (
            'How was Christ exalted in his ascension?',
            'Christ was exalted in his ascension, in that having after his '
            'resurrection often appeared unto and conversed with his apostles, '
            'speaking to them of the things pertaining to the kingdom of God, and '
            'giving them commission to preach the gospel to all nations, forty '
            'days after his resurrection, he, in our nature, and as our head, '
            'triumphing over enemies, visibly went up into the highest heavens, '
            'there to receive gifts for men, to raise up our affections thither, '
            'and to prepare a place for us, where himself is, and shall continue '
            'till his second coming at the end of the world.'),
        54: (
            'How is Christ exalted in his sitting at the right hand of God?',
            'Christ is exalted in his sitting at the right hand of God, in that '
            'as God-man he is advanced to the highest favor with God the Father, '
            'with all fullness of joy, glory, and power over all things in heaven '
            'and earth; and doth gather and defend his church, and subdue their '
            'enemies; furnisheth his ministers and people with gifts and graces, '
            'and maketh intercession for them.'),
        55: ('How doth Christ make intercession?',
             'Christ maketh intercession, by his appearing in our nature '
             'continually before the Father in heaven, in the merit of his '
             'obedience and sacrifice on earth, declaring his will to have it '
             'applied to all believers; answering all accusations against them, '
             'and procuring for them quiet of conscience, notwithstanding daily '
             'failings, access with boldness to the throne of grace, and '
             'acceptance of their persons and services.'),
        56: (
            'How is Christ to be exalted in his coming again to judge the world?',
            'Christ is to be exalted in his coming again to judge the world, in '
            'that he, who was unjustly judged and condemned by wicked men, shall '
            'come again at the last day in great power, and in the full '
            "manifestation of his own glory, and of his Father's, with all his "
            'holy angels, with a shout, with the voice of the archangel, and with '
            'the trumpet of God, to judge the world in righteousness.'),
        57: ('What benefits hath Christ procured by his mediation?',
             'Christ, by his mediation, hath procured redemption, with all other '
             'benefits of the covenant of grace.'),
        58: (
            'How do we come to be made partakers of the benefits which Christ '
            'hath procured?',
            'We are made partakers of the benefits which Christ hath procured, by '
            'the application of them unto us, which is the work especially of God '
            'the Holy Ghost.'),
        59: ('Who are made partakers of redemption through Christ?',
             'Redemption is certainly applied, and effectually communicated, to '
             'all those for whom Christ hath purchased it; who are in time by the '
             'Holy Ghost enabled to believe in Christ according to the gospel.'),
        60: ('Can they who have never heard the gospel, and so know not Jesus '
             'Christ, nor believe in him, be saved by their living according to '
             'the light of nature?',
             'They who, having never heard the gospel, know not Jesus Christ, and '
             'believe not in him, cannot be saved, be they never so diligent to '
             'frame their lives according to the light of nature, or the laws of '
             'that religion which they profess; neither is there salvation in any '
             'other, but in Christ alone, who is the Savior only of his body the '
             'church.'),
        61: ('Are all they saved who hear the gospel, and live in the church?',
             'All that hear the gospel, and live in the visible church, are not '
             'saved; but they only who are true members of the church invisible.'),
        62: ('What is the visible church?',
             'The visible church is a society made up of all such as in all ages '
             'and places of the world do profess the true religion, and of their '
             'children.'),
        63: ('What are the special privileges of the visible church?',
             "The visible church hath the privilege of being under God's special "
             'care and government; of being protected and preserved in all ages, '
             'notwithstanding the opposition of all enemies; and of enjoying the '
             'communion of saints, the ordinary means of salvation, and offers of '
             'grace by Christ to all the members of it in the ministry of the '
             'gospel, testifying, that whosoever believes in him shall be saved, '
             'and excluding none that will come unto him.'),
        64: ('What is the invisible church?',
             'The invisible church is the whole number of the elect, that have '
             'been, are, or shall be gathered into one under Christ the head.'),
        65: ('What special benefits do the members of the invisible church enjoy '
             'by Christ?',
             'The members of the invisible church by Christ enjoy union and '
             'communion with him in grace and glory.'),
        66: ('What is that union which the elect have with Christ?',
             "The union which the elect have with Christ is the work of God's "
             'grace, whereby they are spiritually and mystically, yet really and '
             'inseparably, joined to Christ as their head and husband; which is '
             'done in their effectual calling.'),
        67: (
            'What is effectual calling?',
            "Effectual calling is the work of God's almighty power and grace, "
            'whereby (out of his free and special love to his elect, and from '
            'nothing in them moving him thereunto) he doth, in his accepted time, '
            'invite and draw them to Jesus Christ, by his word and Spirit; '
            'savingly enlightening their minds, renewing and powerfully '
            'determining their wills, so as they (although in themselves dead in '
            'sin) are hereby made willing and able freely to answer his call, and '
            'to accept and embrace the grace offered and conveyed therein.'),
        68: ('Are the elect only effectually called?',
             'All the elect, and they only, are effectually called; although '
             'others may be, and often are, outwardly called by the ministry of '
             'the word, and have some common operations of the Spirit; who, for '
             'their willful neglect and contempt of the grace offered to them, '
             'being justly left in their unbelief, do never truly come to Jesus '
             'Christ.'),
        69: (
            'What is the communion in grace which the members of the invisible '
            'church have with Christ?',
            'The communion in grace which the members of the invisible church '
            'have with Christ, is their partaking of the virtue of his mediation, '
            'in their justification, adoption, sanctification, and whatever else, '
            'in this life, manifests their union with him.'),
        70: (
            'What is justification?',
            "Justification is an act of God's free grace unto sinners, in which "
            'he pardoneth all their sins, accepteth and accounteth their persons '
            'righteous in his sight; not for anything wrought in them, or done by '
            'them, but only for the perfect obedience and full satisfaction of '
            'Christ, by God imputed to them, and received by faith alone.'),
        71:
        ("How is justification an act of God's free grace?",
         'Although Christ, by his obedience and death, did make a proper, '
         "real, and full satisfaction to God's justice in the behalf of them "
         'that are justified; yet inasmuch as God accepteth the satisfaction '
         'from a surety, which he might have demanded of them, and did provide '
         'this surety, his own only Son, imputing his righteousness to them, '
         'and requiring nothing of them for their justification but faith, '
         'which also is his gift, their justification is to them of free grace.'),
        72: (
            'What is justifying faith?',
            'Justifying faith is a saving grace, wrought in the heart of a sinner '
            'by the Spirit and Word of God, whereby he, being convinced of his '
            'sin and misery, and of the disability in himself and all other '
            'creatures to recover him out of his lost condition, not only '
            'assenteth to the truth of the promise of the gospel, but receiveth '
            'and resteth upon Christ and his righteousness, therein held forth, '
            'for pardon of sin, and for the accepting and accounting of his '
            'person righteous in the sight of God for salvation.'),
        73: (
            'How doth faith justify a sinner in the sight of God?',
            'Faith justifies a sinner in the sight of God, not because of those '
            'other graces which do always accompany it, or of good works that are '
            'the fruits of it, nor as if the grace of faith, or any act thereof, '
            'were imputed to him for his justification; but only as it is an '
            'instrument by which he receiveth and applieth Christ and his '
            'righteousness.'),
        74: (
            'What is adoption?',
            'Adoption is an act of the free grace of God, in and for his only Son '
            'Jesus Christ, whereby all those that are justified are received into '
            'the number of his children, have his name put upon them, the Spirit '
            'of his Son given to them, are under his fatherly care and '
            'dispensations, admitted to all the liberties and privileges of the '
            'sons of God, made heirs of all the promises, and fellow-heirs with '
            'Christ in glory.'),
        75: (
            'What is sanctification?',
            "Sanctification is a work of God's grace, whereby they whom God hath, "
            'before the foundation of the world, chosen to be holy, are in time, '
            'through the powerful operation of his Spirit applying the death and '
            'resurrection of Christ unto them, renewed in their whole man after '
            'the image of God; having the seeds of repentance unto life, and all '
            'other saving graces, put into their hearts, and those graces so '
            'stirred up, increased, and strengthened, as that they more and more '
            'die unto sin, and rise unto newness of life.'),
        76: ('What is repentance unto life?',
             'Repentance unto life is a saving grace, wrought in the heart of a '
             'sinner by the Spirit and Word of God, whereby, out of the sight and '
             'sense, not only of the danger, but also of the filthiness and '
             "odiousness of his sins, and upon the apprehension of God's mercy in "
             'Christ to such as are penitent, he so grieves for and hates his '
             'sins, as that he turns from them all to God, purposing and '
             'endeavoring constantly to walk with him in all the ways of new '
             'obedience.'),
        77: (
            'Wherein do justification and sanctification differ?',
            'Although sanctification be inseparably joined with justification, '
            'yet they differ, in that God in justification imputeth the '
            'righteousness of Christ; in sanctification his Spirit infuseth '
            'grace, and enableth to the exercise thereof; in the former, sin is '
            'pardoned; in the other, it is subdued: the one doth equally free all '
            'believers from the revenging wrath of God, and that perfectly in '
            'this life, that they never fall into condemnation; the other is '
            'neither equal in all, nor in this life perfect in any, but growing '
            'up to perfection.'),
        78: (
            'Whence ariseth the imperfection of sanctification in believers?',
            'The imperfection of sanctification in believers ariseth from the '
            'remnants of sin abiding in every part of them, and the perpetual '
            'lustings of the flesh against the spirit; whereby they are often '
            'foiled with temptations, and fall into many sins, are hindered in '
            'all their spiritual services, and their best works are imperfect and '
            'defiled in the sight of God.'),
        79: (
            'May not true believers, by reason of their imperfections, and the '
            'many temptations and sins they are overtaken with, fall away from '
            'the state of grace?',
            'True believers, by reason of the unchangeable love of God, and his '
            'decree and covenant to give them perseverance, their inseparable '
            'union with Christ, his continual intercession for them, and the '
            'Spirit and seed of God abiding in them, can neither totally nor '
            'finally fall away from the state of grace, but are kept by the power '
            'of God through faith unto salvation.'),
        80: (
            'Can true believers be infallibly assured that they are in the estate '
            'of grace, and that they shall persevere therein unto salvation?',
            'Such as truly believe in Christ, and endeavor to walk in all good '
            'conscience before him, may, without extraordinary revelation, by '
            "faith grounded upon the truth of God's promises, and by the Spirit "
            'enabling them to discern in themselves those graces to which the '
            'promises of life are made, and bearing witness with their spirits '
            'that they are the children of God, be infallibly assured that they '
            'are in the estate of grace, and shall persevere therein unto '
            'salvation.'),
        81: (
            'Are all true believers at all times assured of their present being '
            'in the estate of grace, and that they shall be saved?',
            'Assurance of grace and salvation not being of the essence of faith, '
            'true believers may wait long before they obtain it; and, after the '
            'enjoyment thereof, may have it weakened and intermitted, through '
            'manifold distempers, sins, temptations, and desertions; yet are they '
            'never left without such a presence and support of the Spirit of God '
            'as keeps them from sinking into utter despair.'),
        82: ('What is the communion in glory which the members of the invisible '
             'church have with Christ?',
             'The communion in glory which the members of the invisible church '
             'have with Christ, is in this life, immediately after death, and at '
             'last perfected at the resurrection and day of judgment.'),
        83: (
            'What is the communion in glory with Christ which the members of the '
            'invisible church enjoy in this life?',
            'The members of the invisible church have communicated to them in '
            'this life the firstfruits of glory with Christ, as they are members '
            'of him their head, and so in him are interested in that glory which '
            'he is fully possessed of; and, as an earnest thereof, enjoy the '
            "sense of God's love, peace of conscience, joy in the Holy Ghost, and "
            "hope of glory; as, on the contrary, sense of God's revenging wrath, "
            'horror of conscience, and a fearful expectation of judgment, are to '
            'the wicked the beginning of their torments which they shall endure '
            'after death.'),
        84: (
            'Shall all men die?',
            'Death being threatened as the wages of sin, it is appointed unto all '
            'men once to die; for that all have sinned.'),
        85: ('Death being the wages of sin, why are not the righteous delivered '
             'from death, seeing all their sins are forgiven in Christ?',
             'The righteous shall be delivered from death itself at the last day, '
             'and even in death are delivered from the sting and curse of it; so '
             "that, although they die, yet it is out of God's love, to free them "
             'perfectly from sin and misery, and to make them capable of further '
             'communion with Christ in glory, which they then enter upon.'),
        86:
        ('What is the communion in glory with Christ which the members of the '
         'invisible church enjoy immediately after death?',
         'The communion in glory with Christ which the members of the '
         'invisible church enjoy immediately after death, is, in that their '
         'souls are then made perfect in holiness, and received into the '
         'highest heavens, where they behold the face of God in light and '
         'glory, waiting for the full redemption of their bodies, which even '
         'in death continue united to Christ, and rest in their graves as in '
         'their beds, till at the last day they be again united to their souls'),
        87: (
            'What are we to believe concerning the resurrection?',
            'We are to believe that at the last day there shall be a general '
            'resurrection of the dead, both of the just and unjust: when they '
            'that are then found alive shall in a moment be changed; and the '
            'selfsame bodies of the dead which were laid in the grave, being then '
            'again united to their souls forever, shall be raised up by the power '
            'of Christ'),
        88: ('What shall immediately follow after the resurrection?',
             'Immediately after the resurrection shall follow the general and '
             'final judgment of angels and men; the day and hour whereof no man '
             'knoweth, that all may watch and pray, and be ever ready for the '
             'coming of the Lord.'),
        89: ('What shall be done to the wicked at the day of judgment?',
             "At the day of judgment, the wicked shall be set on Christ's left "
             'hand, and, upon clear evidence, and full conviction of their own '
             'consciences, shall have the fearful but just sentence of '
             'condemnation pronounced against them; and thereupon shall be cast '
             'out from the favorable presence of God, and the glorious fellowship '
             'with Christ, his saints, and all his holy angels, into hell, to be '
             'punished with unspeakable torments, both of body and soul, with the '
             'devil and his angels forever.'),
        90: (
            'What shall be done to the righteous at the day of judgment?',
            'At the day of judgment, the righteous, being caught up to Christ in '
            'the clouds, shall be set on his right hand, and there openly '
            'acknowledged and acquitted, shall join with him in the judging of '
            'reprobate angels and men, and shall be received into heaven, where '
            'they shall be fully and forever freed from all sin and misery; '
            'filled with inconceivable joys, made perfectly holy and happy both '
            'in body and soul, in the company of innumerable saints and holy '
            'angels, but especially in the immediate vision and fruition of God '
            'the Father, of our Lord Jesus Christ, and of the Holy Spirit, to all '
            'eternity'),
        91: ('What is the duty which God requireth of man?',
             'The duty which God requireth of man, is obedience to his revealed '
             'will.'),
        92: ('What did God first reveal unto man as the rule of his obedience?',
             'The rule of obedience revealed to Adam in the estate of innocence, '
             'and to all mankind in him, besides a special command not to eat of '
             'the fruit of the tree of the knowledge of good and evil, was the '
             'moral law.'),
        93: ('What is the moral law?',
             'The moral law is the declaration of the will of God to mankind, '
             'directing and binding every one to personal, perfect, and perpetual '
             'conformity and obedience thereunto, in the frame and disposition of '
             'the whole man, soul, and body, and in performance of all those '
             'duties of holiness and righteousness which he oweth to God and man: '
             'promising life upon the fulfilling, and threatening death upon the '
             'breach of it.'),
        94: ('Is there any use of the moral law since the fall?',
             'Although no man, since the fall, can attain to righteousness and '
             'life by the moral law; yet there is great use thereof, as well '
             'common to all men, as peculiar either to the unregenerate, or the '
             'regenerate.'),
        95: (
            'Of what use is the moral law to all men?',
            'The moral law is of use to all men, to inform them of the holy '
            'nature and will of God, and of their duty, binding them to walk '
            'accordingly; to convince them of their disability to keep it, and of '
            'the sinful pollution of their nature, hearts, and lives: to humble '
            'them in the sense of their sin and misery, and thereby help them to '
            'a clearer sight of the need they have of Christ, and of the '
            'perfection of his obedience.'),
        96: ('What particular use is there of the moral law to unregenerate men?',
             'The moral law is of use to unregenerate men, to awaken their '
             'consciences to flee from the wrath to come, and to drive them to '
             'Christ; or, upon the continuance in the estate and way of sin, to '
             'leave them inexcusable, and under the curse thereof.'),
        97: (
            'What special use is there of the moral law to the regenerate?',
            'Although they that are regenerate, and believe in Christ, be '
            'delivered from the moral law as a covenant of works, so as thereby '
            'they are neither justified nor condemned; yet besides the general '
            'uses thereof common to them with all men, it is of special use, to '
            'show them how much they are bound to Christ for his fulfilling it, '
            'and enduring the curse thereof in their stead, and for their good; '
            'and thereby to provoke them to more thankfulness, and to express the '
            'same in their greater care to conform themselves thereunto as the '
            'rule of their obedience.'),
        98: ('Where is the moral law summarily comprehended?',
             'The moral law is summarily comprehended in the Ten Commandments, '
             'which were delivered by the voice of God upon mount Sinai, and '
             'written by him in two tables of stone; and are recorded in the '
             'twentieth chapter of Exodus; the four first commandments containing '
             'our duty to God, and the other six our duty to man.'),
        99: (
            'What rules are to be observed for the right understanding of the Ten '
            'Commandments?',
            'For the right understanding of the Ten Commandments, these rules are '
            'to be observed:'),
        100: ('What special things are we to consider in the Ten Commandments?',
              'We are to consider, in the Ten Commandments, the preface, the '
              'substance of the commandments themselves, and several reasons '
              'annexed to some of them, the more to enforce them.'),
        101: ('What is the preface to the Ten Commandments?',
              'The preface to the Ten Commandments is contained in these words, I '
              'am the LORD thy God, which have brought thee out of the land of '
              'Egypt, out of the house of bondage'),
        102: (
            'What is the sum of the four commandments which contain our duty to '
            'God?',
            'The sum of the four commandments containing our duty to God, is, to '
            'love the Lord our God with all our heart, and with all our soul, '
            'and with all our strength, and with all our mind.'),
        103: (
            'Which is the first commandment?',
            'The first commandment is, Thou shalt have no other gods before me.'),
        104: (
            'What are the duties required in the first commandment?',
            'The duties required in the first commandment are, the knowing and '
            'acknowledging of God to be the only true God, and our God; and to '
            'worship and glorify him accordingly, by thinking, meditating, '
            'remembering, highly esteeming, honoring, adoring, choosing, loving, '
            'desiring, fearing of him; believing him; trusting, hoping, '
            'delighting, rejoicing in him; being zealous for him; calling upon '
            'him, giving all praise and thanks, and yielding all obedience and '
            'submission to him with the whole man; being careful in all things '
            'to please him, and sorrowful when in anything he is offended; and '
            'walking humbly with him.'),
        105: (
            'What are the sins forbidden in the first commandment?',
            'The sins forbidden in the first commandment, are, atheism, in '
            'denying or not having a God; idolatry, in having or worshiping more '
            'gods than one, or any with or instead of the true God; the not '
            'having and avouching him for God, and our God; the omission or '
            'neglect of anything due to him, required in this commandment; '
            'ignorance, forgetfulness, misapprehensions, false opinions, '
            'unworthy and wicked thoughts of him; bold and curious searching '
            'into his secrets; all profaneness, hatred of God; self-love, '
            'self-seeking, and all other inordinate and immoderate setting of '
            'our mind, will, or affections upon other things, and taking them '
            'off from him in whole or in part; vain credulity, unbelief, heresy, '
            'misbelief, distrust, despair, incorrigibleness, and insensibleness '
            'under judgments, hardness of heart, pride, presumption, carnal '
            'security, tempting of God; using unlawful means, and trusting in '
            'lawful means; carnal delights and joys; corrupt, blind, and '
            'indiscreet zeal; lukewarmness, and deadness in the things of God; '
            'estranging ourselves, and apostatizing from God; praying, or giving '
            'any religious worship, to saints, angels, or any other creatures; '
            'all compacts and consulting with the devil, and hearkening to his '
            'suggestions; making men the lords of our faith and conscience; '
            'slighting and despising God and his commands; resisting and '
            'grieving of his Spirit, discontent and impatience at his '
            'dispensations, charging him foolishly for the evils he inflicts on '
            'us; and ascribing the praise of any good we either are, have, or '
            'can do, to fortune, idols, ourselves, or any other creature.'),
        106: ('What are we specially taught by these words, before me, in the '
              'first commandment?',
              'These words, before me, or before my face, in the first '
              'commandment, teach us, that God, who seeth all things, taketh '
              'special notice of, and is much displeased with, the sin of having '
              'any other God: that so it may be an argument to dissuade from it, '
              'and to aggravate it as a most impudent provocation: as also to '
              'persuade us to do as in his sight, whatever we do in his service.'),
        107: (
            'Which is the second commandment?',
            'The second commandment is, Thou shalt not make unto thee any graven '
            'image, or any likeness of anything that is in heaven above, or that '
            'is in the earth beneath, or that is in the water under the earth'),
        108:
        ('What are the duties required in the second commandment?',
         'The duties required in the second commandment are, the receiving, '
         'observing, and keeping pure and entire, all such religious worship '
         'and ordinances as God hath instituted in his word; particularly '
         'prayer and thanksgiving in the name of Christ; the reading, '
         'preaching, and hearing of the word; the administration and '
         'receiving of the sacraments; church government and discipline; the '
         'ministry and maintenance thereof; religious fasting; swearing by '
         'the name of God, and vowing unto him: as also the disapproving, '
         'detesting, opposing, all false worship; and, according to each '
         "one's place and calling, removing it, and all monuments of idolatry."),
        109: (
            'What sins are forbidden in the second commandment?',
            'The sins forbidden in the second commandment are, all devising, '
            'counseling, commanding, using, and any wise approving, any '
            'religious worship not instituted by God himself; the making any '
            'representation of God, of all or of any of the three persons, '
            'either inwardly in our mind, or outwardly in any kind of image or '
            'likeness of any creature whatsoever; all worshiping of it, or God '
            'in it or by it; the making of any representation of feigned '
            'deities, and all worship of them, or service belonging to them; all '
            'superstitious devices, corrupting the worship of God, adding to it, '
            'or taking from it, whether invented and taken up of ourselves, or '
            'received by tradition from others, though under the title of '
            'antiquity, custom, devotion, good intent, or any other pretense '
            'whatsoever; simony; sacrilege; all neglect, contempt, hindering, '
            'and opposing the worship and ordinances which God hath appointed.'),
        110: (
            'What are the reasons annexed to the second commandment, the more to '
            'enforce it?',
            'The reasons annexed to the second commandment, the more to enforce '
            'it, contained in these words, For I the LORD thy God am a jealous '
            'God, visiting the iniquity of the fathers upon the children unto '
            'the third and fourth generation of them that hate me; and shewing '
            'mercy unto thousands of them that love me, and keep my '
            "commandments; are, besides God's sovereignty over us, and propriety "
            'in us, his fervent zeal for his own worship, and his revengeful '
            'indignation against all false worship, as being a spiritual '
            'whoredom; accounting the breakers of this commandment such as hate '
            'him, and threatening to punish them unto divers generations; and '
            'esteeming the observers of it such as love him and keep his '
            'commandments, and promising mercy to them unto many generations.'),
        111: ('Which is the third commandment?',
              'The third commandment is, Thou shalt not take the name of the LORD '
              'thy God in vain: for the LORD will not hold him guiltless that '
              'taketh his name in vain.'),
        112: ('What is required in the third commandment?',
              'The third commandment requires, that the name of God, his titles, '
              'attributes, ordinances, the word, sacraments, prayer, oaths, vows, '
              'lots, his works, and whatsoever else there is whereby he makes '
              'himself known, be holily and reverently used in thought, '
              'meditation, word, and writing; by an holy profession, and '
              'answerable conversation, to the glory of God, and the good of '
              'ourselves, and others.'),
        113: (
            'What are the sins forbidden in the third commandment?',
            'The sins forbidden in the third commandment are, the not using of '
            "God's name as is required; and the abuse of it in an ignorant, "
            'vain, irreverent, profane, superstitious, or wicked mentioning or '
            'otherwise using his titles, attributes, ordinances, or works, by '
            'blasphemy, perjury; all sinful cursings, oaths, vows, and lots; '
            'violating of our oaths and vows, if lawful; and fulfilling them, if '
            'of things unlawful; murmuring and quarreling at, curious prying '
            "into, and misapplying of God's decrees and providences; "
            'misinterpreting, misapplying, or any way perverting the word, or '
            'any part of it, to profane jests, curious or unprofitable '
            'questions, vain janglings, or the maintaining of false doctrines; '
            'abusing it, the creatures, or anything contained under the name of '
            'God, to charms, or sinful lusts and practices; the maligning, '
            "scorning, reviling, or any wise opposing of God's truth, grace, and "
            'ways; making profession of religion in hypocrisy, or for sinister '
            'ends; being ashamed of it, or a shame to it, by unconformable, '
            'unwise, unfruitful, and offensive walking, or backsliding from it.'),
        114: ('What reasons are annexed to the third commandment?',
              'The reasons annexed to the third commandment, in these words, The '
              'LORD thy God, and, For the LORD will not hold him guiltless that '
              'taketh his name in vain, are, because he is the Lord and our God, '
              'therefore his name is not to be profaned, or any way abused by us; '
              'especially because he will be so far from acquitting and sparing '
              'the transgressors of this commandment, as that he will not suffer '
              'them to escape his righteous judgment, albeit many such escape the '
              'censures and punishments of men.'),
        115:
        ('Which is the fourth commandment?',
         'The fourth commandment is, Remember the sabbath day, to keep it holy'),
        116: (
            'What is required in the fourth commandment?',
            'The fourth commandment requireth of all men the sanctifying or '
            'keeping holy to God such set times as he hath appointed in his '
            'word, expressly one whole day in seven; which was the seventh from '
            'the beginning of the world to the resurrection of Christ, and the '
            'first day of the week ever since, and so to continue to the end of '
            'the world; which is the Christian sabbath, and in the New Testament '
            "called The Lord's Day."),
        117: ("How is the sabbath or the Lord's day to be sanctified?",
              "The sabbath or Lord's day is to be sanctified by an holy resting "
              'all the day, not only from such works as are at all times sinful, '
              'but even from such worldly employments and recreations as are on '
              'other days lawful; and making it our delight to spend the whole '
              'time (except so much of it as is to be taken up in works of '
              "necessity and mercy) in the public and private exercises of God's "
              'worship: and, to that end, we are to prepare our hearts, and with '
              'such foresight, diligence, and moderation, to dispose and '
              'seasonably dispatch our worldly business, that we may be the more '
              'free and fit for the duties of that day.'),
        118: (
            'Why is the charge of keeping the sabbath more specially directed to '
            'governors of families, and other superiors?',
            'The charge of keeping the sabbath is more specially directed to '
            'governors of families, and other superiors, because they are bound '
            'not only to keep it themselves, but to see that it be observed by '
            'all those that are under their charge; and because they are prone '
            'ofttimes to hinder them by employments of their own.'),
        119: ('What are the sins forbidden in the fourth commandment?',
              'The sins forbidden in the fourth commandment are, all omissions of '
              'the duties required, all careless, negligent, and unprofitable '
              'performing of them, and being weary of them; all profaning the day '
              'by idleness, and doing that which is in itself sinful; and by all '
              'needless works, words, and thoughts, about our worldly employments '
              'and recreations.'),
        120: (
            'What are the reasons annexed to the fourth commandment, the more to '
            'enforce it?',
            'The reasons annexed to the fourth commandment, the more to enforce '
            'it, are taken from the equity of it, God allowing us six days of '
            'seven for our own affairs, and reserving but one for himself, in '
            'these words, Six days shalt thou labor, and do all thy work: from '
            "God's challenging a special propriety in that day, The seventh day "
            'is the sabbath of the LORD thy God: from the example of God, who in '
            'six days ..'),
        121:
        ('Why is the word Remember set in the beginning of the fourth '
         'commandment?', 'The word Remember is set in the beginning of the fourth '
         'commandment, partly, because of the great benefit of remembering '
         'it, we being thereby helped in our preparation to keep it, and, in '
         'keeping it, better to keep all the rest of the commandments, and to '
         'continue a thankful remembrance of the two great benefits of '
         'creation and redemption, which contain a short abridgment of '
         'religion; and partly, because we are very ready to forget it, for '
         'that there is less light of nature for it, and yet it restraineth '
         'our natural liberty in things at other times lawful; that it cometh '
         'but once in seven days, and many worldly businesses come between, '
         'and too often take off our minds from thinking of it, either to '
         'prepare for it, or to sanctify it; and that Satan with his '
         'instruments much labor to blot out the glory, and even the memory '
         'of it, to bring in all irreligion and impiety.'),
        122: ('What is the sum of the six commandments which contain our duty to '
              'man?',
              'The sum of the six commandments which contain our duty to man, is, '
              'to love our neighbor as ourselves, and to do to others what we '
              'would have them do to us.'),
        123: ('Which is the fifth commandment?',
              'The fifth commandment is, Honour thy father and thy mother: that '
              'thy days may be long upon the land which the Lord thy God giveth '
              'thee.'),
        124: (
            'Who are meant by father and mother in the fifth commandment?',
            'By father and mother, in the fifth commandment, are meant, not only '
            'natural parents, but all superiors in age and gifts; and especially '
            "such as, by God's ordinance, are over us in place of authority, "
            'whether in family, church, or commonwealth.'),
        125: ('Why are superiors styled Father and Mother?',
              'Superiors are styled Father and Mother, both to teach them in all '
              'duties toward their inferiors, like natural parents, to express '
              'love and tenderness to them, according to their several relations; '
              'and to work inferiors to a greater willingness and cheerfulness in '
              'performing their duties to their superiors, as to their parents.'),
        126: ('What is the general scope of the fifth commandment?',
              'The general scope of the fifth commandment is, the performance of '
              'those duties which we mutually owe in our several relations, as '
              'inferiors, superiors or equals.'),
        127: (
            'What is the honor that inferiors owe to their superiors?',
            'The honor which inferiors owe to their superiors is, all due '
            'reverence in heart, word, and behavior; prayer and thanksgiving for '
            'them; imitation of their virtues and graces; willing obedience to '
            'their lawful commands and counsels; due submission to their '
            'corrections; fidelity to, defense, and maintenance of their persons '
            'and authority, according to their several ranks, and the nature of '
            'their places; bearing with their infirmities, and covering them in '
            'love, that so they may be an honor to them and to their government.'),
        128: (
            'What are the sins of inferiors against their superiors?',
            'The sins of inferiors against their superiors are, all neglect of '
            'the duties required toward them; envying at, contempt of, and '
            'rebellion against their persons and places, in their lawful '
            'counsels, commands, and corrections; cursing, mocking, and all such '
            'refractory and scandalous carriage, as proves a shame and dishonor '
            'to them and their government.'),
        129: (
            'What is required of superiors towards their inferiors?',
            'It is required of superiors, according to that power they receive '
            'from God, and that relation wherein they stand, to love, pray for, '
            'and bless their inferiors; to instruct, counsel, and admonish them; '
            'countenancing, commending, and rewarding such as do well; and '
            'discountenancing, reproving, and chastising such as do ill; '
            'protecting, and providing for them all things necessary for soul '
            'and body: and by grave, wise, holy, and exemplary carriage, to '
            'procure glory to God, honor to themselves, and so to preserve that '
            'authority which God hath put upon them.'),
        130: (
            'What are the sins of superiors?',
            'The sins of superiors are, besides the neglect of the duties '
            'required of them, an inordinate seeking of themselves, their own '
            'glory, ease, profit, or pleasure; commanding things unlawful, or '
            'not in the power of inferiors to perform; counseling, encouraging, '
            'or favoring them in that which is evil; dissuading, discouraging, '
            'or discountenancing them in that which is good; correcting them '
            'unduly; careless exposing, or leaving them to wrong, temptation, '
            'and danger; provoking them to wrath; or any way dishonoring '
            'themselves, or lessening their authority, by an unjust, indiscreet, '
            'rigorous, or remiss behavior.'),
        131: ('What are the duties of equals?',
              'The duties of equals are, to regard the dignity and worth of each '
              'other, in giving honor to go one before another; and to rejoice in '
              "each others' gifts and advancement, as their own."),
        132: (
            'What are the sins of equals?',
            'The sins of equals are, besides the neglect of the duties required, '
            'the undervaluing of the worth, envying the gifts, grieving at the '
            'advancement or prosperity one of another; and usurping preeminence '
            'one over another.'),
        133: ('What is the reason annexed to the fifth commandment, the more to '
              'enforce it?',
              'The reason annexed to the fifth commandment, in these words, That '
              'thy days may be long upon the land which the LORD thy God giveth '
              'thee, is an express promise of long life and prosperity, as far as '
              "it shall serve for God's glory and their own good, to all such as "
              'keep this commandment.'),
        134: ('Which is the sixth commandment?',
              'The sixth commandment is, Thou shalt not kill.'),
        135: (
            'What are the duties required in the sixth commandment?',
            'The duties required in the sixth commandment are, all careful '
            'studies, and lawful endeavors, to preserve the life of ourselves '
            'and others by resisting all thoughts and purposes, subduing all '
            'passions, and avoiding all occasions, temptations, and practices, '
            'which tend to the unjust taking away the life of any; by just '
            'defense thereof against violence, patient bearing of the hand of '
            'God, quietness of mind, cheerfulness of spirit; a sober use of '
            'meat, drink, physic, sleep, labor, and recreations; by charitable '
            'thoughts, love, compassion, meekness, gentleness, kindness; '
            'peaceable, mild and courteous speeches and behavior; forbearance, '
            'readiness to be reconciled, patient bearing and forgiving of '
            'injuries, and requiting good for evil; comforting and succoring the '
            'distressed, and protecting and defending the innocent.'),
        136: (
            'What are the sins forbidden in the sixth commandment?',
            'The sins forbidden in the sixth commandment are, all taking away '
            'the life of ourselves, or of others, except in case of public '
            'justice, lawful war, or necessary defense; the neglecting or '
            'withdrawing the lawful and necessary means of preservation of life; '
            'sinful anger, hatred, envy, desire of revenge; all excessive '
            'passions, distracting cares; immoderate use of meat, drink, labor, '
            'and recreations; provoking words, oppression, quarreling, striking, '
            'wounding, and whatsoever else tends to the destruction of the life '
            'of any.'),
        137: ('Which is the seventh commandment?',
              'The seventh commandment is, Thou shalt not commit adultery.'),
        138: ('What are the duties required in the seventh commandment?',
              'The duties required in the seventh commandment are, chastity in '
              'body, mind, affections, words, and behavior; and the preservation '
              'of it in ourselves and others; watchfulness over the eyes and all '
              'the senses; temperance, keeping of chaste company, modesty in '
              'apparel; marriage by those that have not the gift of continency, '
              'conjugal love, and cohabitation; diligent labor in our callings; '
              'shunning all occasions of uncleanness, and resisting temptations '
              'thereunto.'),
        139: ('What are the sins forbidden in the seventh commandment?',
              'The sins forbidden in the seventh commandment, besides the neglect '
              'of the duties required, are, adultery, fornication, rape, incest, '
              'sodomy, and all unnatural lusts; all unclean imaginations, '
              'thoughts, purposes, and affections; all corrupt or filthy '
              'communications, or listening thereunto; wanton looks, impudent or '
              'light behavior, immodest apparel; prohibiting of lawful, and '
              'dispensing with unlawful marriages; allowing, tolerating, keeping '
              'of stews, and resorting to them; entangling vows of single life, '
              'undue delay of marriage; having more wives or husbands than one at '
              'the same time; unjust divorce, or desertion; idleness, gluttony, '
              'drunkenness, unchaste company; lascivious songs, books, pictures, '
              'dancings, stage plays; and all other provocations to, or acts of '
              'uncleanness, either in ourselves or others.'),
        140: ('Which is the eighth commandment?',
              'The eighth commandment is, Thou shalt not steal.'),
        141: (
            'What are the duties required in the eighth commandment?',
            'The duties required in the eighth commandment are, truth, '
            'faithfulness, and justice in contracts and commerce between man and '
            'man; rendering to every one his due; restitution of goods '
            'unlawfully detained from the right owners thereof; giving and '
            'lending freely, according to our abilities, and the necessities of '
            'others; moderation of our judgments, wills, and affections '
            'concerning worldly goods; a provident care and study to get, keep, '
            'use, and dispose these things which are necessary and convenient '
            'for the sustentation of our nature, and suitable to our condition; '
            'a lawful calling, and diligence in it; frugality; avoiding '
            'unnecessary lawsuits, and suretiship, or other like engagements; '
            'and an endeavor, by all just and lawful means, to procure, '
            'preserve, and further the wealth and outward estate of others, as '
            'well as our own.'),
        142: (
            'What are the sins forbidden in the eighth commandment?',
            'The sins forbidden in the eighth commandment, besides the neglect '
            'of the duties required, are, theft, robbery, man-stealing, and '
            'receiving anything that is stolen; fraudulent dealing, false '
            'weights and measures, removing landmarks, injustice and '
            'unfaithfulness in contracts between man and man, or in matters of '
            'trust; oppression, extortion, usury, bribery, vexatious lawsuits, '
            'unjust enclosures and depredation; engrossing commodities to '
            'enhance the price; unlawful callings, and all other unjust or '
            'sinful ways of taking or withholding from our neighbor what belongs '
            'to him, or of enriching ourselves; covetousness; inordinate prizing '
            'and affecting worldly goods; distrustful and distracting cares and '
            'studies in getting, keeping, and using them; envying at the '
            'prosperity of others; as likewise idleness, prodigality, wasteful '
            'gaming; and all other ways whereby we do unduly prejudice our own '
            'outward estate, and defrauding ourselves of the due use and comfort '
            'of that estate which God hath given us.'),
        143: (
            'Which is the ninth commandment?',
            'The ninth commandment is, Thou shalt not bear false witness against '
            'thy neighbour.'),
        144: (
            'What are the duties required in the ninth commandment?',
            'The duties required in the ninth commandment are, the preserving '
            'and promoting of truth between man and man, and the good name of '
            'our neighbor, as well as our own; appearing and standing for the '
            'truth; and from the heart, sincerely, freely, clearly, and fully, '
            'speaking the truth, and only the truth, in matters of judgment and '
            'justice, and in all other things whatsoever; a charitable esteem of '
            'our neighbors; loving, desiring, and rejoicing in their good name; '
            'sorrowing for and covering of their infirmities; freely '
            'acknowledging of their gifts and graces, defending their innocency; '
            'a ready receiving of a good report, and unwillingness to admit of '
            'an evil report, concerning them; discouraging talebearers, '
            'flatterers, and slanderers; love and care of our own good name, and '
            'defending it when need requireth; keeping of lawful promises; '
            'studying and practicing of whatsoever things are true, honest, '
            'lovely, and of good report.'),
        145: (
            'What are the sins forbidden in the ninth commandment?',
            'The sins forbidden in the ninth commandment are, all prejudicing '
            'the truth, and the good name of our neighbors, as well as our own, '
            'especially in public judicature; giving false evidence, suborning '
            'false witnesses, wittingly appearing and pleading for an evil '
            'cause, outfacing and overbearing the truth; passing unjust '
            'sentence, calling evil good, and good evil; rewarding the wicked '
            'according to the work of the righteous, and the righteous according '
            'to the work of the wicked; forgery, concealing the truth, undue '
            'silence in a just cause, and holding our peace when iniquity '
            'calleth for either a reproof from ourselves, or complaint to '
            'others; speaking the truth unseasonably, or maliciously to a wrong '
            'end, or perverting it to a wrong meaning, or in doubtful or '
            'equivocal expressions, to the prejudice of the truth or justice; '
            'speaking untruth, lying, slandering, backbiting, detracting, '
            'talebearing, whispering, scoffing, reviling, rash, harsh, and '
            'partial censuring; misconstructing intentions, words, and actions; '
            'flattering, vainglorious boasting, thinking or speaking too highly '
            'or too meanly of ourselves or others; denying the gifts and graces '
            'of God; aggravating smaller faults; hiding, excusing, or '
            'extenuating of sins, when called to a free confession; unnecessary '
            'discovering of infirmities; raising false rumors, receiving and '
            'countenancing evil reports, and stopping our ears against just '
            'defense; evil suspicion; envying or grieving at the deserved credit '
            'of any; endeavoring or desiring to impair it, rejoicing in their '
            'disgrace and infamy; scornful contempt, fond admiration; breach of '
            'lawful promises; neglecting such things as are of good report, and '
            'practicing, or not avoiding ourselves, or not hindering what we can '
            'in others, such things as procure an ill name.'),
        146: ('Which is the tenth commandment?',
              "The tenth commandment is, Thou shalt not covet thy neighbour's "
              "house, thou shalt not covet thy neighbor's wife, nor his "
              'manservant, nor his maidservant, nor his ox, nor his ass, nor '
              "anything that is thy neighbour's."),
        147: ('What are the duties required in the tenth commandment?',
              'The duties required in the tenth commandment are, such a full '
              'contentment with our own condition, and such a charitable frame of '
              'the whole soul toward our neighbor, as that all our inward motions '
              'and affections touching him, tend unto, and further all that good '
              'which is his.'),
        148: ('What are the sins forbidden in the tenth commandment?',
              'The sins forbidden in the tenth commandment are, discontentment '
              'with our own estate; envying and grieving at the good of our '
              'neighbor, together with all inordinate motions and affections to '
              'anything that is his.'),
        149: (
            'Is any man able perfectly to keep the commandments of God?',
            'No man is able, either of himself, or by any grace received in this '
            'life, perfectly to keep the commandments of God; but doth daily '
            'break them in thought, word, and deed.'),
        150: (
            'Are all transgressions of the law of God equally heinous in '
            'themselves, and in the sight of God?',
            'All transgressions of the law are not equally heinous; but some '
            'sins in themselves, and by reason of several aggravations, are more '
            'heinous in the sight of God than others.'),
        151: ('What are those aggravations that make some sins more heinous than '
              'others?', 'Sins receive their aggravations,'),
        152: (
            'What doth every sin deserve at the hands of God?',
            'Every sin, even the least, being against the sovereignty, goodness, '
            'and holiness of God, and against his righteous law, deserveth his '
            'wrath and curse, both in this life, and that which is to come; and '
            'cannot be expiated but by the blood of Christ.'),
        153: (
            'What doth God require of us, that we may escape his wrath and curse '
            'due to us by reason of the transgression of the law?',
            'That we may escape the wrath and curse of God due to us by reason '
            'of the transgression of the law, he requireth of us repentance '
            'toward God, and faith toward our Lord Jesus Christ, and the '
            'diligent use of the outward means whereby Christ communicates to us '
            'the benefits of his mediation.'),
        154: ('What are the outward means whereby Christ communicates to us the '
              'benefits of his mediation?',
              'The outward and ordinary means whereby Christ communicates to his '
              'church the benefits of his mediation, are all his ordinances; '
              'especially the word, sacraments, and prayer; all which are made '
              'effectual to the elect for their salvation.'),
        155: ('How is the word made effectual to salvation?',
              'The Spirit of God maketh the reading, but especially the preaching '
              'of the word, an effectual means of enlightening, convincing, and '
              'humbling sinners; of driving them out of themselves, and drawing '
              'them unto Christ; of conforming them to his image, and subduing '
              'them to his will; of strengthening them against temptations and '
              'corruptions; of building them up in grace, and establishing their '
              'hearts in holiness and comfort through faith unto salvation.'),
        156: ('Is the Word of God to be read by all?',
              'Although all are not to be permitted to read the word publicly to '
              'the congregation, yet all sorts of people are bound to read it '
              'apart by themselves, and with their families: to which end, the '
              'holy Scriptures are to be translated out of the original into '
              'vulgar languages.'),
        157: (
            'How is the Word of God to be read?',
            'The holy Scriptures are to be read with an high and reverent esteem '
            'of them; with a firm persuasion that they are the very Word of God, '
            'and that he only can enable us to understand them; with desire to '
            'know, believe, and obey the will of God revealed in them; with '
            'diligence, and attention to the matter and scope of them; with '
            'meditation, application, self-denial, and prayer.'),
        158: ('By whom is the Word of God to be preached?',
              'The Word of God is to be preached only by such as are sufficiently '
              'gifted, and also duly approved and called to that office.'),
        159: (
            'How is the Word of God to be preached by those that are called '
            'thereunto?',
            'They that are called to labor in the ministry of the word, are to '
            'preach sound doctrine, diligently, in season and out of season; '
            "plainly, not in the enticing words of man's wisdom, but in "
            'demonstration of the Spirit, and of power; faithfully, making known '
            'the whole counsel of God; wisely, applying themselves to the '
            'necessities and capacities of the hearers; zealously, with fervent '
            'love to God and the souls of his people; sincerely, aiming at his '
            'glory, and their conversion, edification, and salvation.'),
        160: ('What is required of those that hear the word preached?',
              'It is required of those that hear the word preached, that they '
              'attend upon it with diligence, preparation, and prayer; examine '
              'what they hear by the Scriptures; receive the truth with faith, '
              'love, meekness, and readiness of mind, as the Word of God; '
              'meditate, and confer of it; hide it in their hearts, and bring '
              'forth the fruit of it in their lives.'),
        161: (
            'How do the sacraments become effectual means of salvation?',
            'The sacraments become effectual means of salvation, not by any '
            'power in themselves, or any virtue derived from the piety or '
            'intention of him by whom they are administered, but only by the '
            'working of the Holy Ghost, and the blessing of Christ, by whom they '
            'are instituted.'),
        162: (
            'What is a sacrament?',
            'A sacrament is an holy ordinance instituted by Christ in his '
            'church, to signify, seal, and exhibit unto those that are within '
            'the covenant of grace, the benefits of his mediation; to strengthen '
            'and increase their faith, and all other graces; to oblige them to '
            'obedience; to testify and cherish their love and communion one with '
            'another; and to distinguish them from those that are without.'),
        163: ('What are the parts of a sacrament?',
              'The parts of a sacrament are two; the one an outward and sensible '
              "sign, used according to Christ's own appointment; the other an "
              'inward and spiritual grace thereby signified.'),
        164: ('How many sacraments hath Christ instituted in his church under the '
              'New Testament?',
              'Under the New Testament Christ hath instituted in his church only '
              "two sacraments, baptism and the Lord's supper."),
        165: (
            'What is baptism?',
            'Baptism is a sacrament of the New Testament, wherein Christ hath '
            'ordained the washing with water in the name of the Father, and of '
            'the Son, and of the Holy Ghost, to be a sign and seal of ingrafting '
            'into himself, of remission of sins by his blood, and regeneration '
            'by his Spirit; of adoption, and resurrection unto everlasting life; '
            'and whereby the parties baptized are solemnly admitted into the '
            'visible church, and enter into an open and professed engagement to '
            "be wholly and only the Lord's."),
        166: (
            'Unto whom is baptism to be administered?',
            'Baptism is not to be administered to any that are out of the '
            'visible church, and so strangers from the covenant of promise, till '
            'they profess their faith in Christ, and obedience to him, but '
            'infants descending from parents, either both, or but one of them, '
            'professing faith in Christ, and obedience to him, are in that '
            'respect within the covenant, and to be baptized.'),
        167: (
            'How is baptism to be improved by us?',
            'The needful but much neglected duty of improving our baptism, is to '
            'be performed by us all our life long, especially in the time of '
            'temptation, and when we are present at the administration of it to '
            'others; by serious and thankful consideration of the nature of it, '
            'and of the ends for which Christ instituted it, the privileges and '
            'benefits conferred and sealed thereby, and our solemn vow made '
            'therein; by being humbled for our sinful defilement, our falling '
            'short of, and walking contrary to, the grace of baptism, and our '
            'engagements; by growing up to assurance of pardon of sin, and of '
            'all other blessings sealed to us in that sacrament; by drawing '
            'strength from the death and resurrection of Christ, into whom we '
            'are baptized, for the mortifying of sin, and quickening of grace; '
            'and by endeavoring to live by faith, to have our conversation in '
            'holiness and righteousness, as those that have therein given up '
            'their names to Christ; and to walk in brotherly love, as being '
            'baptized by the same Spirit into one body.'),
        168: (
            "What is the Lord's supper?",
            "The Lord's supper is a sacrament of the New Testament, wherein, by "
            'giving and receiving bread and wine according to the appointment of '
            'Jesus Christ, his death is showed forth; and they that worthily '
            'communicate feed upon his body and blood, to their spiritual '
            'nourishment and growth in grace; have their union and communion '
            'with him confirmed; testify and renew their thankfulness, and '
            'engagement to God, and their mutual love and fellowship each with '
            'other, as members of the same mystical body.'),
        169: (
            'How hath Christ appointed bread and wine to be given and received '
            "in the sacrament of the Lord's supper?",
            'Christ hath appointed the ministers of his word, in the '
            "administration of this sacrament of the Lord's supper, to set apart "
            'the bread and wine from common use, by the word of institution, '
            'thanksgiving, and prayer; to take and break the bread, and to give '
            'both the bread and the wine to the communicants: who are, by the '
            'same appointment, to take and eat the bread, and to drink the wine, '
            'in thankful remembrance that the body of Christ was broken and '
            'given, and his blood shed, for them.'),
        170: (
            "How do they that worthily communicate in the Lord's supper feed "
            'upon the body and blood of Christ therein?',
            'As the body and blood of Christ are not corporally or carnally '
            "present in, with, or under the bread and wine in the Lord's supper, "
            'and yet are spiritually present to the faith of the receiver, no '
            'less truly and really than the elements themselves are to their '
            'outward senses; so they that worthily communicate in the sacrament '
            "of the Lord's supper, do therein feed upon the body and blood of "
            'Christ, not after a corporal and carnal, but in a spiritual manner; '
            'yet truly and really, while by faith they receive and apply unto '
            'themselves Christ crucified, and all the benefits of his death.'),
        171: (
            "How are they that receive the sacrament of the Lord's supper to "
            'prepare themselves before they come unto it?',
            "They that receive the sacrament of the Lord's supper are, before "
            'they come, to prepare themselves thereunto, by examining themselves '
            'of their being in Christ, of their sins and wants; of the truth and '
            'measure of their knowledge, faith, repentance; love to God and the '
            'brethren, charity to all men, forgiving those that have done them '
            'wrong; of their desires after Christ, and of their new obedience; '
            'and by renewing the exercise of these graces, by serious '
            'meditation, and fervent prayer.'),
        172: (
            'May one who doubteth of his being in Christ, or of his due '
            "preparation, come to the Lord's supper?",
            'One who doubteth of his being in Christ, or of his due preparation '
            "to the sacrament of the Lord's supper, may have true interest in "
            "Christ, though he be not yet assured thereof; and in God's account "
            'hath it, if he be duly affected with the apprehension of the want '
            'of it, and unfeignedly desires to be found in Christ, and to depart '
            'from iniquity: in which case (because promises are made, and this '
            'sacrament is appointed, for the relief even of weak and doubting '
            'Christians) he is to bewail his unbelief, and labor to have his '
            'doubts resolved; and, so doing, he may and ought to come to the '
            "Lord's supper, that he may be further strengthened."),
        173: ("May any who profess the faith, and desire to come to the Lord's "
              'supper, be kept from it?',
              'Such as are found to be ignorant or scandalous, notwithstanding '
              "their profession of the faith, and desire to come to the Lord's "
              'supper, may and ought to be kept from that sacrament, by the power '
              'which Christ hath left in his church, until they receive '
              'instruction, and manifest their reformation.'),
        174: (
            "What is required of them that receive the sacrament of the Lord's "
            'supper in the time of the administration of it?',
            "It is required of them that receive the sacrament of the Lord's "
            'supper, that, during the time of the administration of it, with all '
            'holy reverence and attention they wait upon God in that ordinance, '
            'diligently observe the sacramental elements and actions, heedfully '
            "discern the Lord's body, and affectionately meditate on his death "
            'and sufferings, and thereby stir up themselves to a vigorous '
            'exercise of their graces; in judging themselves, and sorrowing for '
            'sin; in earnest hungering and thirsting after Christ, feeding on '
            'him by faith, receiving of his fullness, trusting in his merits, '
            'rejoicing in his love, giving thanks for his grace; in renewing of '
            'their covenant with God, and love to all the saints.'),
        175: (
            'What is the duty of Christians, after they have received the '
            "sacrament of the Lord's supper?",
            'The duty of Christians, after they have received the sacrament of '
            "the Lord's supper, is seriously to consider how they have behaved "
            'themselves therein, and with what success; if they find quickening '
            'and comfort, to bless God for it, beg the continuance of it, watch '
            'against relapses, fulfill their vows, and encourage themselves to a '
            'frequent attendance on that ordinance: but if they find no present '
            'benefit, more exactly to review their preparation to, and carriage '
            'at, the sacrament; in both which, if they can approve themselves to '
            'God and their own consciences, they are to wait for the fruit of it '
            'in due time: but, if they see they have failed in either, they are '
            'to be humbled, and to attend upon it afterwards with more care and '
            'diligence.'),
        176: (
            "Wherein do the sacraments of baptism and the Lord's supper agree?",
            "The sacraments of baptism and the Lord's supper agree, in that the "
            'author of both is God; the spiritual part of both is Christ and his '
            'benefits; both are seals of the same covenant, are to be dispensed '
            'by ministers of the gospel, and by none other; and to be continued '
            'in the church of Christ until his second coming.'),
        177: ("Wherein do the sacraments of baptism and the Lord's supper differ?",
              "The sacraments of baptism and the Lord's supper differ, in that "
              'baptism is to be administered but once, with water, to be a sign '
              'and seal of our regeneration and ingrafting into Christ, and that '
              "even to infants; whereas the Lord's supper is to be administered "
              'often, in the elements of bread and wine, to represent and exhibit '
              'Christ as spiritual nourishment to the soul, and to confirm our '
              'continuance and growth in him, and that only to such as are of '
              'years and ability to examine themselves.'),
        178: (
            'What is prayer?',
            'Prayer is an offering up of our desires unto God, in the name of '
            'Christ, by the help of his Spirit; with confession of our sins, and '
            'thankful acknowledgement of his mercies.'),
        179: (
            'Are we to pray unto God only?',
            'God only being able to search the hearts, hear the requests, pardon '
            'the sins, and fulfill the desires of all; and only to be believed '
            'in, and worshiped with religious worship; prayer, which is a '
            'special part thereof, is to be made by all to him alone, and to '
            'none other.'),
        180: (
            'What is it to pray in the name of Christ?',
            'To pray in the name of Christ is, in obedience to his command, and '
            'in confidence on his promises, to ask mercy for his sake; not by '
            'bare mentioning of his name, but by drawing our encouragement to '
            'pray, and our boldness, strength, and hope of acceptance in prayer, '
            'from Christ and his mediation.'),
        181: (
            'Why are we to pray in the name of Christ?',
            'The sinfulness of man, and his distance from God by reason thereof, '
            'being so great, as that we can have no access into his presence '
            'without a mediator; and there being none in heaven or earth '
            'appointed to, or fit for, that glorious work but Christ alone, we '
            'are to pray in no other name but his only.'),
        182: (
            'How doth the Spirit help us to pray?',
            'We not knowing what to pray for as we ought, the Spirit helpeth our '
            'infirmities, by enabling us to understand both for whom, and what, '
            'and how prayer is to be made; and by working and quickening in our '
            'hearts (although not in all persons, nor at all times, in the same '
            'measure) those apprehensions, affections, and graces which are '
            'requisite for the right performance of that duty.'),
        183: ('For whom are we to pray?',
              'We are to pray for the whole church of Christ upon earth; for '
              'magistrates, and ministers; for ourselves, our brethren, yea, our '
              'enemies; and for all sorts of men living, or that shall live '
              'hereafter; but not for the dead, nor for those that are known to '
              'have sinned the sin unto death.'),
        184: ('For what things are we to pray?',
              'We are to pray for all things tending to the glory of God, the '
              "welfare of the church, our own or others' good; but not for "
              'anything that is unlawful.'),
        185: (
            'How are we to pray?',
            'We are to pray with an awful apprehension of the majesty of God, '
            'and deep sense of our own unworthiness, necessities, and sins; with '
            'penitent, thankful, and enlarged hearts; with understanding, faith, '
            'sincerity, fervency, love, and perseverance, waiting upon him, with '
            'humble submission to his will.'),
        186: (
            'What rule hath God given for our direction in the duty of prayer?',
            'The whole Word of God is of use to direct us in the duty of prayer; '
            'but the special rule of direction is that form of prayer which our '
            "Savior Christ taught his disciples, commonly called The Lord's "
            'prayer.'),
        187: ("How is the Lord's prayer to be used?",
              "The Lord's prayer is not only for direction, as a pattern, "
              'according to which we are to make other prayers; but may also be '
              'used as a prayer, so that it be done with understanding, faith, '
              'reverence, and other graces necessary to the right performance of '
              'the duty of prayer.'),
        188: ("Of how many parts doth the Lord's prayer consist?",
              "The Lord's prayer consists of three parts; a preface, petitions, "
              'and a conclusion.'),
        189: (
            "What doth the preface of the Lord's prayer teach us?",
            "The preface of the Lord's prayer (contained in these words, Our "
            'Father which art in heaven) teacheth us, when we pray, to draw near '
            'to God with confidence of his fatherly goodness, and our interest '
            'therein; with reverence, and all other childlike dispositions, '
            'heavenly affections, and due apprehensions of his sovereign power, '
            'majesty, and gracious condescension: as also, to pray with and for '
            'others.'),
        190: ('What do we pray for in the first petition?',
              'In the first petition (which is, Hallowed be thy name), '
              'acknowledging the utter inability and indisposition that is in '
              'ourselves and all men to honor God aright, we pray, that God would '
              'by his grace enable and incline us and others to know, to '
              'acknowledge, and highly to esteem him, his titles, attributes, '
              'ordinances, word, works, and whatsoever he is pleased to make '
              'himself known by; and to glorify him in thought, word, and deed: '
              'that he would prevent and remove atheism, ignorance, idolatry, '
              'profaneness, and whatsoever is dishonorable to him; and, by his '
              'overruling providence, direct and dispose of all things to his own '
              'glory.'),
        191: (
            'What do we pray for in the second petition?',
            'In the second petition (which is, Thy kingdom come), acknowledging '
            'ourselves and all mankind to be by nature under the dominion of sin '
            'and Satan, we pray, that the kingdom of sin and Satan may be '
            'destroyed, the gospel propagated throughout the world, the Jews '
            'called, the fullness of the Gentiles brought in; the church '
            'furnished with all gospel officers and ordinances, purged from '
            'corruption, countenanced and maintained by the civil magistrate; '
            'that the ordinances of Christ may be purely dispensed, and made '
            'effectual to the converting of those that are yet in their sins, '
            'and the confirming, comforting, and building up of those that are '
            'already converted: that Christ would rule in our hearts here, and '
            'hasten the time of his second coming, and our reigning with him '
            'forever: and that he would be pleased so to exercise the kingdom of '
            'his power in all the world, as may best conduce to these ends.'),
        192: (
            'What do we pray for in the third petition?',
            'In the third petition (which is, Thy will be done in earth, as it '
            'is in heaven), acknowledging that by nature we and all men are not '
            'only utterly unable and unwilling to know and to do the will of '
            'God, but prone to rebel against his word, to repine and murmur '
            'against his providence, and wholly inclined to do the will of the '
            'flesh, and of the devil: we pray, that God would by his Spirit take '
            'away from ourselves and others all blindness, weakness, '
            'indisposedness, and perverseness of heart; and by his grace make us '
            'able and willing to know, do, and submit to his will in all things, '
            'with the like humility, cheerfulness, faithfulness, diligence, '
            'zeal, sincerity, and constancy, as the angels do in heaven.'),
        193: (
            'What do we pray for in the fourth petition?',
            'In the fourth petition (which is, Give us this day our daily '
            'bread), acknowledging that in Adam, and by our own sin, we have '
            'forfeited our right to all the outward blessings of this life, and '
            'deserve to be wholly deprived of them by God, and to have them '
            'cursed to us in the use of them; and that neither they of '
            'themselves are able to sustain us, nor we to merit, or by our own '
            'industry to procure them; but prone to desire, get, and use them '
            'unlawfully: we pray for ourselves and others, that both they and '
            'we, waiting upon the providence of God from day to day in the use '
            'of lawful means, may, of his free gift, and as to his fatherly '
            'wisdom shall seem best, enjoy a competent portion of them; and have '
            'the same continued and blessed unto us in our holy and comfortable '
            'use of them, and contentment in them; and be kept from all things '
            'that are contrary to our temporal support and comfort.'),
        194: (
            'What do we pray for in the fifth petition?',
            'In the fifth petition (which is, Forgive us our debts, as we '
            'forgive our debtors), acknowledging that we and all others are '
            'guilty both of original and actual sin, and thereby become debtors '
            'to the justice of God; and that neither we, nor any other creature, '
            'can make the least satisfaction for that debt: we pray for '
            'ourselves and others, that God of his free grace would, through the '
            'obedience and satisfaction of Christ, apprehended and applied by '
            'faith, acquit us both from the guilt and punishment of sin, accept '
            'us in his Beloved; continue his favor and grace to us, pardon our '
            'daily failings, and fill us with peace and joy, in giving us daily '
            'more and more assurance of forgiveness; which we are the rather '
            'emboldened to ask, and encouraged to expect, when we have this '
            'testimony in ourselves, that we from the heart forgive others their '
            'offenses.'),
        195: (
            'What do we pray for in the sixth petition?',
            'In the sixth petition (which is, And lead us not into temptation, '
            'but deliver us from evil), acknowledging that the most wise, '
            'righteous, and gracious God, for divers holy and just ends, may so '
            'order things, that we may be assaulted, foiled, and for a time led '
            'captive by temptations; that Satan, the world, and the flesh, are '
            'ready powerfully to draw us aside, and ensnare us; and that we, '
            'even after the pardon of our sins, by reason of our corruption, '
            'weakness, and want of watchfulness, are not only subject to be '
            'tempted, and forward to expose ourselves unto temptations, but also '
            'of ourselves unable and unwilling to resist them, to recover out of '
            'them, and to improve them; and worthy to be left under the power of '
            'them; we pray, that God would so overrule the world and all in it, '
            'subdue the flesh, and restrain Satan, order all things, bestow and '
            'bless all means of grace, and quicken us to watchfulness in the use '
            'of them, that we and all his people may by his providence be kept '
            'from being tempted to sin; or, if tempted, that by his Spirit we '
            'may be powerfully supported and enabled to stand in the hour of '
            'temptation; or when fallen, raised again and recovered out of it, '
            'and have a sanctified use and improvement thereof: that our '
            'sanctification and salvation may be perfected, Satan trodden under '
            'our feet, and we fully freed from sin, temptation, and all evil, '
            'forever.'),
        196: (
            "What doth the conclusion of the Lord's prayer teach us?",
            "The conclusion of the Lord's prayer (which is, For thine is the "
            'kingdom, and the power, and the glory, forever. Amen.) teacheth us '
            'to enforce our petitions with arguments, which are to be taken, not '
            'from any worthiness in ourselves, or in any other creature, but '
            'from God; and with our prayers to join praises, ascribing to God '
            'alone eternal sovereignty, omnipotency, and glorious excellency; in '
            'regard whereof, as he is able and willing to help us, so we by '
            'faith are emboldened to plead with him that he would, and quietly '
            'to rely upon him, that he will fulfill our requests. And, to '
            'testify this our desire and assurance, we say, Amen.')
    }
    output = ''
    for x in range(start, stop+1):
        output += "Question " + str(x) + ". "
        output += doc[x][0]
        output += doc[x][1]
    return output


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Westminster Confession and Catechisms. " \
                    "Ask Reformed Bot to read a Confession Chapter and " \
                    "paragraph or a Catechism question to you."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Ask Reformed Bot to read a Confession Chapter and " \
                    "paragraph or a Catechism question to you."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        

def error_response(doc=None, error=None):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Request Not Understood"
    speech_output = ''
    if doc:
        speech_output += doc + ". "
    if error:
        speech_output += error + ". "
    
    speech_output += "I did not understand your request.  The Westminster Confession " \
                    "has 33 chapters, the shorter Catechism has 107 questions and " \
                    "the Larger Catechism has 196 questions. "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "The Westminster Confession has 33 chapters, the shorter Catechism " \
                    "has 107 questions and the Larger Catechism has 196 questions. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for studying with Reformed bot."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def validate_address(intent, doc):
    limits = {1:10,2:3,3:8,4:2,5:7,6:6,7:6,8:8,9:5,10:4,11:6,12:1,13:3,14:3,15:6,16:7,17:3,18:4,19:7,20:4,21:8,22:7,23:4,24:6,25:6,26:3,27:5,28:7,29:8,30:4,31:4,32:3,33:3}
    
    if doc == "wcf":
        chap = None
        if 'value' in intent['slots']['Chapter']:
            try:
                chap = int(intent['slots']['Chapter']['value'])
                if not (1 <= chap <= 33):
                    return -1, -1, -1, -1, "Error Code 01"
            except:
                pass
                
        q1 = None
        if 'value' in intent['slots']['QueryUno']:
            try:
                q1 = int(intent['slots']['QueryUno']['value'])
                if not (1 <= q1 <= limits[chap]):
                    return -1, -1, -1, -1, "Error Code 02"
            except:
                pass
        
        if chap and 'value' in intent['slots']['Paragraph']:
            try:
                par = int(intent['slots']['Paragraph']['value'])
                if not (1 <= par <= limits[chap]):
                    return -1, -1, -1, -1, "Error Code 03"
                return chap, par, par, limits[chap], "No Error"
            except:
                pass
            
        
        if chap and q1 and 'value' in intent['slots']['QueryDos']:
            try:
                q2 = int(intent['slots']['QueryDos']['value'])
                if not (1 <= q2 <= limits[chap]):
                    return -1, -1, -1, -1, "Error Code 04"
                if q2 < q1:
                    q2 = q1
                return chap, q1, q2, limits[chap], "No Error"
            except:
                pass
            
        if chap and 'value' in intent['slots']['Finisher']:
            if q1:
                return chap, q1, limits[chap], limits[chap], "No Error"
                
            if chap:
                return chap, 1, limits[chap], limits[chap], "No Error"
            
            return -1, -1, -1, -1, "Error Code 05"  # shouldn't get this far
        
        if chap:
            return chap, 1, limits[chap], limits[chap], "No Error"
            
        return -1, -1, -1, -1, "Error Code 06" # shouldn't get this far

    if doc == "wsc":
        chap = None
        if 'value' in intent['slots']['Chapter']:
            chap = int(intent['slots']['Chapter']['value'])
            if not (1 <= chap <= 107):
                return -1, -1, -1, -1, "Error Code 07"
                
        q1 = None
        if 'value' in intent['slots']['QuestionUno']:
            q1 = int(intent['slots']['QuestionUno']['value'])
            if not (1 <= q1 <= 107):
                return -1, -1, -1, -1, "Error Code 08"
                
        if chap:
            return -1, chap, chap, 107, "No Error"
            
        if 'value' in intent['slots']['QuestionDos']:
            q2 = int(intent['slots']['QuestionDos']['value'])
            if not (1 <= q2 <= 107):
                return -1, -1, -1, -1, "Error Code 09"
            if q2 < q1:
                q2 = q1
            return -1, q1, q2, 107, "No Error"
                
        if q1:
            return -1, q1, q1, 107, "No Error"
            
        if 'value' in intent['slots']['Finisher']:
            return -1, q1, 107, 107, "No Error"
            
        return -1, -1, -1, -1, "Error Code 10" # should not get this far
        
    # Else WLC
    chap = None
    if 'value' in intent['slots']['Chapter']:
        chap = int(intent['slots']['Chapter']['value'])
        if not (1 <= chap <= 196):
            return -1, -1, -1, -1, "Error Code 11"
            
    q1 = None
    if 'value' in intent['slots']['QuestionUno']:
        q1 = int(intent['slots']['QuestionUno']['value'])
        if not (1 <= q1 <= 196):
            return -1, -1, -1, -1, "Error Code 12"
            
    if chap:
        return -1, chap, chap, 196, "No Error"
        
    if 'value' in intent['slots']['QuestionDos']:
        q2 = int(intent['slots']['QuestionDos']['value'])
        if not (1 <= q2 <= 196):
            return -1, -1, -1, -1, "Error Code 13"
        if q2 < q1:
            q2 = q1
        return -1, q1, q2, 196, "No Error"
                
    if q1:
        return -1, q1, q1, 196, "No Error"
        
    if 'value' in intent['slots']['Finisher']:
        return -1, q1, 196, 196, "No Error"
        
    return -1, -1, -1, -1, "Error Code 14" # should not get this far


def get_ducment(intent, session):
    doc = None
    
    if 'value' in intent['slots']['Document']: # Document specified
        if intent['slots']['Document']['value'].lower() in ("westminster confession of faith", 
                                            "confession of faith", "wcf", "confession", "w. c. f."):
            doc = 'wcf'
            
        elif intent['slots']['Document']['value'].lower() in ("westminster shorter catechism", 
                                            "shorter catechism", "catechism", "wsc", "w. s. c"):
            doc = 'wsc'
            
        else:
            doc = 'wlc'
            
    elif session.get('attributes', {}) and 'Document' in session.get('attributes', {}):
        doc = session['attributes']['Document']
        
    elif 'value' in intent['slots']['QuestionUno']:
        doc = 'wsc'
        
    elif 'value' in intent['slots']['Chapter']:
        doc = 'wcf'
    
    return doc


def get_westminster_ref(intent, session):
    session_attributes = {}
    should_end_session = False
    chapter = -1
    fwd = True
    
    doc = get_ducment(intent, session)
    
    if not doc:
        speech_output = "Which document are you interested in? " \
                        "The Westminster documents are a Confession of " \
                        "Faith along with Shorter and Larger Catechisms."
        reprompt_text = "Which document are you interested in?"
        return build_response(session_attributes, build_speechlet_response(
            intent['name'], speech_output, reprompt_text, should_end_session))
    
    session_attributes.update({'Document':doc})
    
    
    if 'value' not in intent['slots']['Context']:
        (chapter, start, stop, end, error) = validate_address(intent, doc)
        if start == -1:
            return error_response(doc, error)
        if stop != start:
            stop = start+1 # Only show two at a time regardless of inquiry
            if stop > end:
                stop = end
        if chapter > 0:
            session_attributes.update({'Chapter':chapter})
        session_attributes.update({'Start':start})
        session_attributes.update({'Stop':stop})
        session_attributes.update({'End':end})
        session_attributes.update({'Forward':True})
    elif session.get('attributes', {}) and 'Start' in session.get('attributes', {}):
        if 'value' in intent['slots']['Chapter']:
            chapter = session['attributes']['Chapter']
        start = session['attributes']['Start']
        stop = session['attributes']['Stop']
        end = session['attributes']['End']
        fwd = session['attributes']['Forward']
        context = intent['slots']['Context']['value'].lower()
        # no
        if context in ("no", "no thanks", "no thank you"):
            return handle_session_end_request()
        # previous | back | last one
        elif context in ("back", "previous", "last one"):
            fwd = False
        # more | keep going | please | yes please | yup | duh | uh huh | continue | yes | next
        elif context in ("more","keep going","please","yes please","yup","duh","uh huh","continue","yes","next"):
            inc = stop - start
            if fwd:
                start = stop + 1
                if start > end:
                    start = end
            else:
                start = stop - 1
                if start < 1:
                    start = 1
            stop = start + inc # This will probably work...
            if stop < 1:
                stop = 1
            elif stop > end:
                stop = end
        # again | repeat | one more again | once more | one more time
        else:
            pass # no change needed
    else:
        return error_response()
        
    if chapter > 0:
        session_attributes.update({'Chapter':chapter})
    session_attributes.update({'Start':start})
    session_attributes.update({'Stop':stop})
    session_attributes.update({'End':end})
    session_attributes.update({'Forward':fwd})
    
    if doc == "wcf":
        card_title = "Westminster Confession of Faith"
        first = not (session.get('attributes', {}) and 'Start' in session.get('attributes', {}))
        speech_output = get_confession(first, chapter, start, stop)
    elif doc == "wsc":
        card_title = "Westminster Shorter Catechism"
        speech_output = get_shorter_catechism(start, stop)
    else:
        card_title = "Westminster Larger Catechism"
        speech_output = get_larger_catechism(start, stop)
    
    if end == stop or (not fwd and start == 1):
        reprompt_text = None
        should_end_session = True
    else:
        speech_output += " Would you like to hear more?"
        reprompt_text = "Would you like to hear more?"
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "RefReq":
        return get_westminster_ref(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.c3e1252d-e318-4e73-bcea-69ebb88f09c2"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
