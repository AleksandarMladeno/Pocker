curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": 2,
        "suit": "C"
    },
    {
        "value": "A",
        "suit": "S"
    },
    {
        "value": 5,
        "suit": "D"
    },
    {
        "value": 4,
        "suit": "H"
    },
    {
        "value": "J",
        "suit": "C"
    }
]'