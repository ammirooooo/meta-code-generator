# Generated from C:/Users/Dell/PycharmProjects/Project-Compiler/XMLGrammar\XMLLexer.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,18,231,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,
        4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,
        12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,
        18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,
        1,0,1,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,78,8,1,10,1,12,1,81,9,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,91,8,2,10,2,12,2,94,9,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,4,4,108,8,4,11,4,12,
        4,109,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,119,8,4,11,4,12,4,120,1,4,
        1,4,3,4,125,8,4,1,5,1,5,3,5,129,8,5,1,5,4,5,132,8,5,11,5,12,5,133,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,9,4,9,159,8,9,11,9,12,9,160,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,14,1,14,1,15,1,15,5,15,183,8,15,10,15,12,15,186,9,15,1,15,
        1,15,1,15,5,15,191,8,15,10,15,12,15,194,9,15,1,15,3,15,197,8,15,
        1,16,1,16,5,16,201,8,16,10,16,12,16,204,9,16,1,17,1,17,1,17,1,17,
        1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,3,20,218,8,20,1,21,3,21,
        221,8,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,3,59,79,92,
        0,24,3,1,5,2,7,3,9,4,11,5,13,6,15,7,17,8,19,0,21,9,23,10,25,11,27,
        12,29,13,31,14,33,15,35,16,37,17,39,0,41,0,43,0,45,0,47,18,49,0,
        3,0,1,2,10,2,0,9,9,32,32,2,0,38,38,60,60,2,0,34,34,60,60,2,0,39,
        39,60,60,3,0,9,10,13,13,32,32,3,0,48,57,65,70,97,102,1,0,48,57,2,
        0,45,46,95,95,3,0,183,183,768,879,8255,8256,8,0,58,58,65,90,97,122,
        8304,8591,11264,12271,12289,55295,63744,64975,65008,65533,241,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,
        1,0,0,0,1,25,1,0,0,0,1,27,1,0,0,0,1,29,1,0,0,0,1,31,1,0,0,0,1,33,
        1,0,0,0,1,35,1,0,0,0,1,37,1,0,0,0,2,47,1,0,0,0,2,49,1,0,0,0,3,51,
        1,0,0,0,5,66,1,0,0,0,7,86,1,0,0,0,9,99,1,0,0,0,11,124,1,0,0,0,13,
        131,1,0,0,0,15,135,1,0,0,0,17,139,1,0,0,0,19,149,1,0,0,0,21,158,
        1,0,0,0,23,162,1,0,0,0,25,166,1,0,0,0,27,171,1,0,0,0,29,176,1,0,
        0,0,31,178,1,0,0,0,33,196,1,0,0,0,35,198,1,0,0,0,37,205,1,0,0,0,
        39,209,1,0,0,0,41,211,1,0,0,0,43,217,1,0,0,0,45,220,1,0,0,0,47,222,
        1,0,0,0,49,227,1,0,0,0,51,52,5,60,0,0,52,53,5,33,0,0,53,54,5,45,
        0,0,54,55,5,45,0,0,55,59,1,0,0,0,56,58,9,0,0,0,57,56,1,0,0,0,58,
        61,1,0,0,0,59,60,1,0,0,0,59,57,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,
        0,62,63,5,45,0,0,63,64,5,45,0,0,64,65,5,62,0,0,65,4,1,0,0,0,66,67,
        5,60,0,0,67,68,5,33,0,0,68,69,5,91,0,0,69,70,5,67,0,0,70,71,5,68,
        0,0,71,72,5,65,0,0,72,73,5,84,0,0,73,74,5,65,0,0,74,75,5,91,0,0,
        75,79,1,0,0,0,76,78,9,0,0,0,77,76,1,0,0,0,78,81,1,0,0,0,79,80,1,
        0,0,0,79,77,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,93,0,0,83,
        84,5,93,0,0,84,85,5,62,0,0,85,6,1,0,0,0,86,87,5,60,0,0,87,88,5,33,
        0,0,88,92,1,0,0,0,89,91,9,0,0,0,90,89,1,0,0,0,91,94,1,0,0,0,92,93,
        1,0,0,0,92,90,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,62,0,0,
        96,97,1,0,0,0,97,98,6,2,0,0,98,8,1,0,0,0,99,100,5,38,0,0,100,101,
        3,35,16,0,101,102,5,59,0,0,102,10,1,0,0,0,103,104,5,38,0,0,104,105,
        5,35,0,0,105,107,1,0,0,0,106,108,3,41,19,0,107,106,1,0,0,0,108,109,
        1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,112,
        5,59,0,0,112,125,1,0,0,0,113,114,5,38,0,0,114,115,5,35,0,0,115,116,
        5,120,0,0,116,118,1,0,0,0,117,119,3,39,18,0,118,117,1,0,0,0,119,
        120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,
        123,5,59,0,0,123,125,1,0,0,0,124,103,1,0,0,0,124,113,1,0,0,0,125,
        12,1,0,0,0,126,132,7,0,0,0,127,129,5,13,0,0,128,127,1,0,0,0,128,
        129,1,0,0,0,129,130,1,0,0,0,130,132,5,10,0,0,131,126,1,0,0,0,131,
        128,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,
        14,1,0,0,0,135,136,5,60,0,0,136,137,1,0,0,0,137,138,6,6,1,0,138,
        16,1,0,0,0,139,140,5,60,0,0,140,141,5,63,0,0,141,142,5,120,0,0,142,
        143,5,109,0,0,143,144,5,108,0,0,144,145,1,0,0,0,145,146,3,37,17,
        0,146,147,1,0,0,0,147,148,6,7,1,0,148,18,1,0,0,0,149,150,5,60,0,
        0,150,151,5,63,0,0,151,152,1,0,0,0,152,153,3,35,16,0,153,154,1,0,
        0,0,154,155,6,8,2,0,155,156,6,8,3,0,156,20,1,0,0,0,157,159,8,1,0,
        0,158,157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,
        0,161,22,1,0,0,0,162,163,5,62,0,0,163,164,1,0,0,0,164,165,6,10,4,
        0,165,24,1,0,0,0,166,167,5,63,0,0,167,168,5,62,0,0,168,169,1,0,0,
        0,169,170,6,11,4,0,170,26,1,0,0,0,171,172,5,47,0,0,172,173,5,62,
        0,0,173,174,1,0,0,0,174,175,6,12,4,0,175,28,1,0,0,0,176,177,5,47,
        0,0,177,30,1,0,0,0,178,179,5,61,0,0,179,32,1,0,0,0,180,184,5,34,
        0,0,181,183,8,2,0,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,
        0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,197,5,34,
        0,0,188,192,5,39,0,0,189,191,8,3,0,0,190,189,1,0,0,0,191,194,1,0,
        0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,192,1,0,
        0,0,195,197,5,39,0,0,196,180,1,0,0,0,196,188,1,0,0,0,197,34,1,0,
        0,0,198,202,3,45,21,0,199,201,3,43,20,0,200,199,1,0,0,0,201,204,
        1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,36,1,0,0,0,204,202,1,
        0,0,0,205,206,7,4,0,0,206,207,1,0,0,0,207,208,6,17,0,0,208,38,1,
        0,0,0,209,210,7,5,0,0,210,40,1,0,0,0,211,212,7,6,0,0,212,42,1,0,
        0,0,213,218,3,45,21,0,214,218,7,7,0,0,215,218,3,41,19,0,216,218,
        7,8,0,0,217,213,1,0,0,0,217,214,1,0,0,0,217,215,1,0,0,0,217,216,
        1,0,0,0,218,44,1,0,0,0,219,221,7,9,0,0,220,219,1,0,0,0,221,46,1,
        0,0,0,222,223,5,63,0,0,223,224,5,62,0,0,224,225,1,0,0,0,225,226,
        6,22,4,0,226,48,1,0,0,0,227,228,9,0,0,0,228,229,1,0,0,0,229,230,
        6,23,2,0,230,50,1,0,0,0,19,0,1,2,59,79,92,109,120,124,128,131,133,
        160,184,192,196,202,217,220,5,6,0,0,5,1,0,3,0,0,5,2,0,4,0,0
    ]

class XMLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INSIDE = 1
    PROC_INSTR = 2

    COMMENT = 1
    CDATA = 2
    DTD = 3
    EntityRef = 4
    CharRef = 5
    SEA_WS = 6
    OPEN = 7
    XMLDeclOpen = 8
    TEXT = 9
    CLOSE = 10
    SPECIAL_CLOSE = 11
    SLASH_CLOSE = 12
    SLASH = 13
    EQUALS = 14
    STRING = 15
    Name = 16
    S = 17
    PI = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "INSIDE", "PROC_INSTR" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "CDATA", "DTD", "EntityRef", "CharRef", "SEA_WS", 
            "OPEN", "XMLDeclOpen", "TEXT", "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", 
            "SLASH", "EQUALS", "STRING", "Name", "S", "PI" ]

    ruleNames = [ "COMMENT", "CDATA", "DTD", "EntityRef", "CharRef", "SEA_WS", 
                  "OPEN", "XMLDeclOpen", "SPECIAL_OPEN", "TEXT", "CLOSE", 
                  "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", "EQUALS", "STRING", 
                  "Name", "S", "HEXDIGIT", "DIGIT", "NameChar", "NameStartChar", 
                  "PI", "IGNORE" ]

    grammarFileName = "XMLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


