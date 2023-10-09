from marshmallow import Schema, fields


class BookValidation(Schema):   # Checks for the Book_Schema
    title = fields.String(required=True)
    author_name = fields.String(required=True)
    serial = fields.String(required=True)


class CustomerValidation(Schema):   # Checks for the Customer Schema
    name = fields.String(required=True)

