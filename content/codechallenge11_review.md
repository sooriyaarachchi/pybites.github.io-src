Title: Code Challenge 11 - Generators for Fun and Profit - Review
Date: 2017-03-25 09:10
Category: Challenges
Tags: codechallenges, code review, learning, yield, Counter, glob, regex
Slug: codechallenge11_review
Authors: PyBites
Summary: It's end of the week again so we review the [code challenge of this week](http://pybit.es/codechallenge11.html). It's never late to sign up, just fork our [challenges repo](https://github.com/pybites/challenges) and start coding.
cover: images/featured/pb-challenge.png

It's end of the week again so we review the code challenge of this week: [Generators for Fun and Profit](http://pybit.es/codechallenge11.html). It's never late to join, just [fork us](https://github.com/pybites/challenges) and start coding.

## Our solution + learning

This was a pretty easy one, yet showing a powerful way to start thinking about generators as pipelines that can be plugged into each other.

Our solution is [here](https://github.com/pybites/challenges/blob/solutions/11/generators.py). A couple of notes:

* Here you see the 'plugged into each other' part:

        if __name__ == "__main__":
            files = gen_files('../*/*.py')
            lines = gen_lines(files)
            modules = gen_grep(lines, re.compile(r'^import (\w+)'))
            ...

* iglob returns an iterator which yields the paths matching a pathname pattern, glob returns a list, also fine because we are not dealing with a lot of directories. You can also use os.walk but when you have a clear pattern (i)glob is less code.

* We use yield from (>= 3.3) which saves a for loop (shorter).

* As [seen before](http://pybit.es/codechallenge03_review.html) use collections.Counter, it's hard to beat short- and conciseness:

        def gen_count(modules):
            yield from Counter(modules).most_common()

* We use grouping to capture the match as discussed in [our regex article](http://pybit.es/mastering-regex.html):

        def gen_grep(lines, pattern):
            for line in lines:
                m = pattern.match(line.rstrip())
                if m:
                    yield m.group(1)  # retrieves what's matched in parenthesis

        modules = gen_grep(lines, re.compile(r'^import (\w+)'))

## Community branch

We got our first solution PR which we merged onto our [community branch](https://github.com/pybites/challenges/tree/community). This is a nice way to get credit and help our community learn more. 

[The solution](https://github.com/pybites/challenges/blob/community/11/generators-atakume.py) was pretty similar to ours. One nice addition was to sort manually on both values and keys, most_common only sorts by values. Also the regex part was slightly different stripping off import with re.sub. It is nice to see different solutions to the same problem, you learn more.

## next(Challenges)

Next week we do another game, so we expect some more complexity and variety in solutions. Stay tuned ...

## Do you like these challenges?

We hope you are enjoying this. If we can do anything better or you have ideas please [open a new issue](https://github.com/pybites/challenges/issues/new) or reach out to us. See you next week ...
