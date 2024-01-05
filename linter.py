import re
from SublimeLinter.lint import Linter, LintMatch

class Generic(Linter):
    cmd = '__cmd__'
    regex = (
        r'^(?P<message>.+)$'
    )
    multiline = False
    defaults = {
        'selector': ''
    }

    def split_match(self, match):
        self.name = self.settings.get('name') or attrs.get('name') or cls_name.lower()
        error = super().split_match(match)
        rematch = re.compile(self.settings.get('regexp')).match(error['message'])
        if type(rematch).__name__ == 'NoneType':
            return error

        # error = super().split_match(rematch) # this will duplicate annotations
        # "match", "line", "col", "error", "warning", "message", "near", "filename",
        # "error_type", "code", "end_line", "end_col"

        reerror = LintMatch(rematch.groupdict())
        error['match'] = rematch
        error['line'] = self.apply_line_base(reerror.get('line'))
        error['end_line'] = self.apply_line_base(reerror.get('end_line'))
        error['end_col'] = self.apply_col_base(reerror.get('end_col'))

        col = reerror.get('col')
        if col and not col.isdigit():
            error['col'] = len(col)
        else:
            error['col'] = self.apply_col_base(col)

        error['error'] = reerror.get('error')
        error['warning'] = reerror.get('warning')
        error['message'] = reerror.get('message')
        error['near'] = reerror.get('near')
        error['filename'] = reerror.get('filename')
        error['error_type'] = reerror.get('error_type')
        error['code'] = reerror.get('code')

        return error
