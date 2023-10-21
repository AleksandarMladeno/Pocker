curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "name": 2,
        "suit": "C"
    },
    {
        "name": "A",
        "suit": "S"
    },
    {
        "name": 5,
        "suit": "D"
    },
    {
        "name": 4,
        "suit": "H"
    },
    {
        "name": "J",
        "suit": "C"
    }
]'