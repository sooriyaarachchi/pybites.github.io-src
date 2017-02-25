Title: Code Challenge 05 - Twitter data analysis Part 2: similar tweeters - review
Date: 2017-02-10 23:00
Category: Challenges
Tags: codechallenges, code review, learning, nlp, Twitter, twitterapi, gensim, nltk
Slug: codechallenge05_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge05.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge05.html). It's never late to join, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.

## Learning

This week's challenge was really hard. We looked at [Gensim](https://radimrehurek.com/gensim/) to calculate similarity between Twitter users.

Below what we got. Any feedback welcome. Code is [here](https://github.com/pybites/challenges/blob/solutions/05/).

* First we tweaked usertweets.py from last week to download 200 tweets of 15 users and store them as csv files in the data/ subdirectory. Users are mostly Pythonistas, but also some unrelated. We changed the solution a bit: instead of comparing only two users, we rank similarity of one user of the set against all others.

* We load all tweets per user in with get_user_tokens() and tokenize them with: 

		def tokenize_text(words):
			words = [word for word in words if len(word) > 4 and word not in STOPWORDS]
			words = [word for word in words if _is_ascii(word)]
			words = [word for word in words if not IS_LINK_OBJ.search(word)]
			return words

	Where IS_LINK_OBJ discards links and mentions:

		IS_LINK_OBJ = re.compile(r'^(?:@|https?://)')

	We get stopwords from nltk:

		from nltk.corpus import stopwords
		STOPWORDS = set(stopwords.words('english'))

	The underscore methods are helpers. We assigned lambdas to variables, but flake8 complained, so better methods :)

* Then we use Gensim to compare a user against the set. This took quite some effort, hopefully our method is correct, the results (see further down) look promosing. We partially used [this thread](http://stackoverflow.com/questions/22433884/python-gensim-how-to-calculate-document-similarity-using-the-lda-model).

		from gensim import corpora, models, similarities

		data = []
		for du in diff_users:  # globbing csv files in data/ or provided with sys.argv[1:]
			data.append(get_user_tokens(du))
		dictionary = corpora.Dictionary(data)

		corpus = [dictionary.doc2bow(text) for text in data]
		lda = models.ldamodel.LdaModel(corpus, num_topics=5,
									id2word=dictionary, passes=15)

		index = similarities.MatrixSimilarity(lda[corpus])

		tokens = get_user_tokens(user)
		vec_bow = dictionary.doc2bow(tokens)
		vec_lda = lda[vec_bow]

		sims = index[vec_lda]
		sims = sorted(enumerate(sims), key=lambda item: -item[1])
		for i, sim in sims:
			print(diff_users[i], sim)

	Full code [here](https://github.com/pybites/challenges/blob/solutions/05/).

* Interestingly this model worked kind of ok, but got different results upon running and not much polarity. It turned out that the sample Twitter set (200 tweets per user) was too small, so we created a data/new directory and used [yanofsky's awesome tweet_dumper](https://gist.github.com/yanofsky/5436496) to get 3200 tweets per user. 

	Data set before vs after:

		$ wc -l *|grep total
			3618 total
		$ wc -l new/*|grep total
		   45573 total

	This did not make sense due to small data set:

		$ python similar_tweeters.py Pybonacci
		cine_tv_es 0.999743 -> nothing to do yet almost 1.0 ?!
		github 0.999743
		gvanrossum 0.455312
		...

	With the new data set, although the script takes longer to run, now the results are much better:
	
		# not much Python: 
		$ python similar_tweeters.py paugasol
		jsonmez 0.739746
		Schwarzenegger 0.739746
		tferriss 0.739746
		cine_tv_es 0.631373
		gvanrossum 0.631373
		treyhunner 0.631373
		bbelderbos 0.206394
		dbader_org 0.206394
		newsafaribooks 0.206394
		techmoneykids 0.113994
		github 0.0983753
		lifehacker 0.0983753
		pybites 0.056072
		importpython 0.0432182
		PythonEggs 0.0432182
		raymondh 0.0432182

		# more Py
		$ python similar_tweeters.py pybites
		dbader_org 0.936956
		importpython 0.936956
		PythonEggs 0.936956
		tferriss 0.936956 -> not sure about this one
		bbelderbos 0.367078
		techmoneykids 0.340996
		github 0.320053
		newsafaribooks 0.320053
		gvanrossum 0.138829
		jsonmez 0.138829
		lifehacker 0.138829
		Schwarzenegger 0.138829
		treyhunner 0.138829
		raymondh 0.0201458
		cine_tv_es 0.0
		paugasol 0.0
		
		# results change upon second run - comment if you know why / how to fix or improve?
		$ python similar_tweeters.py pybites
		importpython 0.890289
		newsafaribooks 0.890289
		PythonEggs 0.890289
		bbelderbos 0.506814
		techmoneykids 0.443702
		jsonmez 0.426503
		paugasol 0.426503
		Schwarzenegger 0.426503
		tferriss 0.426503
		github 0.138233
		gvanrossum 0.138233
		treyhunner 0.138233
		dbader_org 0.100782 -> was high last run ?!
		lifehacker 0.0658598
		raymondh 0.0658598
		cine_tv_es 0.0451122

	Running one more, my personal Twitter. Also a lot of Python at the top, jsonmez/ tferriss/ pybites I have mentioned/retweeted more than once. This looks pretty good ...

		$ python similar_tweeters.py bbelderbos
		dbader_org 0.985021
		gvanrossum 0.985021
		importpython 0.985021
		jsonmez 0.985021
		pybites 0.985021
		PythonEggs 0.985021
		tferriss 0.985021
		treyhunner 0.985021
		techmoneykids 0.275167
		newsafaribooks 0.149423
		paugasol 0.149423
		Schwarzenegger 0.149423
		raymondh 0.142598
		cine_tv_es 0.064402
		github 0.064402
		lifehacker 0.0570781

* This was not an easy challenge! However we learned a lot: our first NLP exploration, playing with a relatively complex library and discovering the data science part of it: the quality of your input data.

## Any issues or feedback?

What did you learn this challenge? Feel free to share you code in the comments below. 

How are you experiencing these challenges? You like the format? What can we do differently and/or better?

## next(challenges)

Next week we pause a bit from Twitter doing something new and original on Monday, stay tuned ...

Again to start coding [fork our challenges repo](https://github.com/pybites/challenges) or [sync it](https://help.github.com/articles/syncing-a-fork/) if you already forked it.
