curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": "A",
        "suit": "S"
    },
    {
        "value": "A",
        "suit": "D"
    },
    {
        "value": "A",
        "suit": "C"
    },
    {
        "value": "4",
        "suit": "H"
    },
    {
        "value": "5",
        "suit": "S"
    }
]'