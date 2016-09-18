(remove, blocked, active, editor, writer) = (-1, 0, 1, 2, 3)
USER_STATUS_CHOICES = [
        (writer, ("writer")),
        (editor, ("editor")),
        (active, ("active")),
        (blocked, ("blocked")),
        (remove, ("remove")),
    ]


Man = u'M'
Woman = u'F'
Other = u'O'
GENDER_CHOICES = (
        (Man, ('man')),
        (Woman, ('woman')),
        (Other, ('other')),
    )