"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["name"],
            "answer": "name",
        },
        {
            "input": ["name#"],
            "answer": "nam",
        },
        {
            "input": ["na##me"],
            "answer": "me",
        },
        {
            "input": ["nam#e#"],
            "answer": "na",
        },
        {
            "input": ["##name"],
            "answer": "name",
        },
        {
            "input": ["name######"],
            "answer": "",
        },
        {
            "input": ["nam######e"],
            "answer": "e",
        },
        {
            "input": ["n###ame"],
            "answer": "ame",
        },
        {
            "input": ["thna#m##e"],
            "answer": "the",
        },
        {
            "input": ["oppo##r##t##u###nity"],
            "answer": "nity",
        },
    ],
    "Extra": [
        {
            "input": ["if you #had o##n##e## shot#### o#r one opp#o##r###tunity"],
            "answer": "if youh  r onetunity",
        },
    ]
}
