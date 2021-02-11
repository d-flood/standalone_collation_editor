#-*- coding: utf-8 -*-

class RuleConditions(object):

    def ignore_unclear(self, decision_word, token_words):
        decision_word = decision_word.replace('_', '')
        decision_word = decision_word.replace('\u0323', '')
        token_words = [w.replace('_', '') for w in token_words]
        token_words = [w.replace('\u0323', '') for w in token_words]
        return(decision_word, token_words)

    def ignore_supplied(self, decision_word, token_words):
        decision_word = decision_word.replace('[', '').replace(']', '')
        token_words = [w.replace('[', '').replace(']', '') for w in token_words]
        return(decision_word, token_words)


class ApplySettings(object):

    def lower_case(self, token):
        token['interface'] = token['interface'].lower()
        return token

    def hide_supplied_text(self, token):
        token['interface'] = token['interface'].replace('[', '').replace(']', '')
        return token

    def hide_unclear_text(self, token):
        token['interface'] = token['interface'].replace('_', '')
        token['interface'] = token['interface'].replace('\u0323', '')
        return token
