curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": "2",
        "suit": "S"
    },
    {
        "value": "3",
        "suit": "S"
    },
    {
        "value": "4",
        "suit": "S"
    },
    {
        "value": "5",
        "suit": "S"
    },
    {
        "value": "6",
        "suit": "S"
    }
]'