Title: Watch Me Code - Solving Bite 21. Query a Nested Data Structure
Date: 2018-07-14 16:00
Category: CodeChalleng.es
Tags: dict, list, beginner, data structures, bites of py, video, sum, list comprehension, dictionary comprehension
Slug: nested-data-structure-exercise
Authors: Bob
Summary: I recorded a video solving [Bite 21. Query a nested data structure](https://codechalleng.es/bites/21/). The exercise presents us with a dictionary of car manufacturers and their corresponding car models. We will extract various bits and pieces from it as well as sort the nested model lists. This is a common type of data structure so specially for a beginner it is important to have this become second nature. Prepare to learn more about looping, some string operations, and list / dict comprehensions.
cover: images/featured/pb-article.png

I recorded a video solving [Bite 21. Query a nested data structure](https://codechalleng.es/bites/21/). The exercise presents us with a dictionary of car manufacturers and their corresponding car models. We will extract various bits and pieces from it as well as sort the nested model lists. This is a common type of data structure so specially for a beginner it is important to have this become second nature. Prepare to learn more about looping, some string operations, and list / dict comprehensions.

## Warning

Before watching the solution video, we highly encourage you to follow [this promo link](https://codechalleng.es/bites/promo/datastructures) and try it yourself. Seriously, you learn n times more by having tried it yourself and comparing your solution to ours or via the Bite Forum feature (see at the end of the video). Enjoy!

### Ready for the solution?

<div class="container">
<iframe src="https://www.youtube.com/embed/Yk13k-_QZ-U" frameborder="0" allowfullscreen class="video"></iframe>
</div>

## Takeaways

- When you don't need `(key, value)` pairs, instead of `items` you can use `keys()` or `values()`.

- `join` is a super handy string method to know about: `return ', '.join(cars['Jeep'])`

- List comprehensions are one of our favorite features, I write them from the inside out and would probably not use more than one for loop: `return [models[0] for models in cars.values()]`

- You can flatten a list of lists like this: `models = sum(cars.values(), [])`

- You can use a dictionary comprehension to modify an existing dict and returning a new dict, all in one go:

		return {manufacturer: sorted(models) for
				manufacturer, models in cars.items()}

	It doesn't really matter here but just to note: `sorted` returns a new list object, while `list.sort()` would sort in-place.

- We defined this Bite some time ago, and I forgot about some parts of the solution. This served two purposes: 

	- Making mistakes and/or not coming to the best solution at first is actually a good thing. This is part of the learning: going through the struggle and contrasting an earlier iteration with a later one.
	- It is good to know that once solved you can go back after some time and use a Bite to refresh your knowledge!

- As you saw towards the end we have a forum for each Bite now where you can share / discuss your solution with other community members. This will only add to the learning. Note this is only accessible if you have resolved the Bite to avoid any spoilers. 

### Help

If you are stuck and don't want to use the _solution button_ - after all this would deduct points (unless it's an Intro Bite) - you can ask for help using our #codechallenges Slack channel. To join our Slack [confirm your email on our platform](http://codechalleng.es), then opt-in to Slack under _Settings_.

## What did you learn?

Where there other insights you got while doing this Bite exercise? We hope to salute you on the platform and Slack. And remember ...

---

Keep Calm and Code in Python!

-- Bob
