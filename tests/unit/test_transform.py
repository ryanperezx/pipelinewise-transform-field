import unittest
import hashlib

from transform_field import transform


class TestTransform(unittest.TestCase):
    """
    Unit Tests for the transform module
    """

    def setUp(self) -> None:
        self.config = {}

    def test_set_null(self):
        """TEST SET-NULL transformation"""
        self.assertEqual(
            transform.do_transform({"col_1": "John"}, "col_1", "SET-NULL"),
            None
        )

    def test_hash(self):
        """Test HASH transformation"""
        self.assertEqual(
            transform.do_transform({"col_1": "John"}, "col_1", "HASH"),
            hashlib.sha256("John".encode('utf-8')).hexdigest()
        )

    def test_polyline(self):
        """Test HASH transformation"""
        polyline= r"an~{HydvZ~@]h@O|@Y~@[rC}@jCy@lEwAbEqAvDoAzE}AFE???@?@?@@??@?@@??@Hn@DZFTLb@JTLPRPnAn@pCxAPPRZPd@H`@`@bF@`@DVPrBFxA@b@JfD??Gj@ADCDA@IFwAG_AAi@?k@?mA?W?uA@a@@G?A@EDGHY?W?_@@_@@S@WBUBg@Dk@Hi@H}@PQFcATgAZA@qA`@eEpAa@NCD]b@qCz@[JC@a@LyCbA_DdA_K~Cm@TGBKBk@RwIjCsEpAYHA@YJqA^??cJhCi@PmCv@sEfAe@Je@LSBs@L]FMDa@FiARcANUB{@HmCP_BJu@FQ@A?S@w@Fm@L_@PIDa@XQNOPSTOVEFKP[n@MXK\Wx@ITWfACPEXIx@?BEj@CNE|@A`@AF?X?b@?b@@x@@VBx@Fj@Fv@F`@F`@F^Ll@h@lCf@lCr@tDF\Nr@BNj@`Db@bC^|BJl@^tB`@bCBPLt@Lv@^zBZ`BZnA??v@jG`ArH\nCx@xHv@bID`@TfCXlD\fENfCj@bIVzD@LBZ@NTfERhEBd@@B?NV`FZbGf@`JFdAVvEPvBP`BJl@N|@Lv@H`@\zAHZH\Vx@L`@`@nAj@zAh@zAPb@Xx@d@tA`@tAZhABHXtAP|@NbAR~AJbAH`ANdCFdBHbBBp@Bp@V`Hb@rM@d@Bd@@ZBb@J|BJfCXlFPbDDx@@NLjBNzBvAlTFx@ThDd@hHDt@FdAXvERvCNzBJrALtAJ`AH`Ah@xDRvABHHh@DNPbAXtA`@bBRv@z@dDFRFTv@rCvAhFf@dBb@~ARr@j@rBjB`Hv@rCHV^xAXnAXrARdALr@Lt@@NHd@L`ATrBP~AL~ALnAPrBJfA??CP?L?R?RD`@HbANbBHfAHp@@JNdAL`AP~@H`@F^H^H\H^BJDNT~@HZH^Vx@X|@p@nBVr@Vr@Zz@h@xAPb@Tn@JXFPRh@Vt@Tj@DJd@tAL\FLDLJ\?@JXFXHb@D^BV@H?N@R?PANAd@Gb@EZI^MZMVGLGLOTQVQRGHKLEDEDADGFGNmAtAsA|AW\KLa@f@c@h@q@`AKLiA|AILs@bAUZc@r@KNs@dA_@j@[b@Y`@Y^}@lAY^A@]^}BnCgApAGHc@h@e@h@q@x@eBxBs@z@oAzAwAbBGHuBfCmAxAIJeBrBUVIJ_@b@EFc@f@QR?@WXo@v@q@v@ORQPoCdD}@dAuBdCeD|DuBbCMLuChDaBlByBjCc@f@sBfC]^sBdCmC~C]`@EFIH[`@wCjDwA~AED_Az@kA|@gAv@cBlAqHpFuCvBiDbCiChBeM`JaD|BUNUPaAr@mDfCkAz@kE|CIDkCrBkAz@UPkBpAsCnBoBvA_BlAYNWPaAl@uF`EmBtAUNq@f@kBrAcAr@kBrA_@Vg@XUJc@Ts@Zw@X_AZi@P}E~AwAb@gA`@kErAoC|@mC|@gBj@eGpBqA`@c@NiCx@sA`@sDhAw@XcC~@}Bt@uA`@QHc@La@NkCx@}@XGBa@LkCx@u@VmCz@o@ReA\iGtBsDjAgCz@iC~@sC|@yBr@cBf@aGjBw@VwFpBkBn@sA`@WJ{Bn@oA`@oKhDc@Nc@LsC~@uEzAw@X}Br@sDjAcAb@c@Pg@Vk@XKFi@Zw@d@]Vc@Za@Z]Xg@b@m@n@_@^MN{@`AQTe@h@WXQTyDvE[^e@l@k@r@c@h@{@dAk@p@_AjAcApA]b@u@|@s@x@c@j@MNc@f@y@`AWZMNKLEDABMPA?GJEDIJaLdNqChDkAxAmAvA[`@?@QRyAfBeBxBa@f@g@j@g@l@o@v@m@t@{@fAy@`As@|@q@x@e@j@o@x@c@f@EDa@f@w@`AaAjAiBzBe@j@{@dAGFMPo@t@wAfBCBc@h@e@h@q@z@y@bAs@|@c@j@q@x@QTa@f@c@f@c@j@a@f@q@x@c@f@o@x@i@n@i@n@i@p@Y\i@p@}@hAQRMNGHCBaAjA_BlBwBlCqChDiC|CeAnAk@p@o@v@q@x@s@x@oArA}@z@e@`@s@h@k@`@e@Xy@f@{@`@i@T}@\}@Xg@L_ATqAVsAV{@P??e@GO?e@Hq@Jw@H[BO@]@[?U?O?m@CaAE_BIi@AQ?M?U@QBA?QBSD[HMDQFEB]PWP[R]V[VSNs@h@YRCB[RGD_@RYNYHUHWFA?i@Ji@Jm@L??iB\gARe@H}Bb@eB\sAVy@ReBb@eBj@??UCC?E?EAC?GECAKIE]CYCWAU?W?S@S@QBQDO?CDODOHOFKHKLKDGHEFEFCPENAR@PBPFJHFDLLLPLTLXL^n@nBFRh@~Ad@rAr@pBFRRf@`@hA`@fAn@dB\`AHPHPDHFHLLh@rAZv@Zv@Zv@JRHTLVp@`BVj@Xl@Th@^v@^x@b@~@r@xAj@fAn@nAd@|@\p@T^??X|@f@bAn@vAn@vATn@b@jAZt@p@|A`@~@LVR`@DRBR??Yb@sBpDi@|@iApBKVMVOVMXIH?@EHEFGLGHaAjBeAjBA?A?A?A@A?A?A@A@A@A?A@?@ABA@?@ABA@?@?BAB?@?B?@?B?@?@?@?@?@?@?@uDfGyDhG??RZRXFNHNfAbBvB~Cx@nAx@nAR\TZpApBpArB??Wl@k@dAYj@Ud@EFEH??EHEJs@~As@|Ao@xAo@zAMTKTw@bBw@bBo@zAq@zAMX]r@Wh@}@pAY`@wA|B??DJHTb@`Bf@hBRp@"
        distance= "13.064203654600199"
        self.assertEqual(
            transform.do_transform({"col_1": polyline}, "col_1", "GPOLYLINE-DISTANCE"),
            distance
        )

    def test_mask_date(self):
        """Test MASK-DATE transformation"""
        self.assertEqual(
            transform.do_transform({"col_1": "2019-05-21"}, "col_1", "MASK-DATE"),
            "2019-01-01T00:00:00"
        )

        # Mask date should keep the time elements
        self.assertEqual(
            transform.do_transform({"col_1": "2019-05-21T13:34:11"}, "col_1", "MASK-DATE"),
            "2019-01-01T13:34:11"
        )

        # Mask date should keep the time elements, date is invalid
        self.assertEqual(
            transform.do_transform({"col_1": "2019-05-21T13:34:99"}, "col_1", "MASK-DATE"),
            "2019-05-21T13:34:99"
        )

    def test_mask_number(self):
        """Test MASK-NUMBER transformation"""
        self.assertEqual(
            transform.do_transform({"col_1": "1234567890"}, "col_1", "MASK-NUMBER"),
            0
        )

    def test_mask_hidden(self):
        """Test MASK-HIDDEN transformation"""
        self.assertEqual(
            transform.do_transform({"col_1": "abakadabra123"}, "col_1", "MASK-HIDDEN"),
            'hidden'
        )

    def test_mask_string_skip_ends_case1(self):
        """Test MASK-STRING-SKIP-ENDS transformation with n=3"""
        self.assertEqual(
            transform.do_transform({"col_1": "do!maskme!"}, "col_1", "MASK-STRING-SKIP-ENDS-3"),
            'do!****me!'
        )

    def test_mask_string_skip_ends_case2(self):
        """Test MASK-STRING-SKIP-ENDS transformation with n=2"""
        self.assertEqual(
            transform.do_transform({"col_1": "nomask"}, "col_1", "MASK-STRING-SKIP-ENDS-2"),
            'no**sk'
        )

    def test_mask_string_skip_ends_case3(self):
        """Test MASK-STRING-SKIP-ENDS transformation where string length equals to 2 * mask_length"""
        self.assertEqual(
            transform.do_transform({"col_1": "nomask"}, "col_1", "MASK-STRING-SKIP-ENDS-3"),
            '******'
        )

    def test_mask_string_skip_ends_case4(self):
        """Test MASK-STRING-SKIP-ENDS transformation where string length less than 2 * mask_length"""
        self.assertEqual(
            transform.do_transform({"col_1": "shortmask"}, "col_1", "MASK-STRING-SKIP-ENDS-5"),
            '*********'
        )

    def test_unknown_transformation_type(self):
        """Test not existing transformation type"""
        # Should return the original value
        self.assertEqual(
            transform.do_transform({"col_1": "John"}, "col_1", "NOT-EXISTING-TRANSFORMATION-TYPE"),
            "John"
        )

    def test_conditions(self):
        """Test conditional transformations"""

        # Matching condition: Should transform to NULL
        self.assertEqual(
            transform.do_transform(
                # Record:
                {"col_1": "random value", "col_2": "passwordHash", "col_3": "lkj"},
                # Column to transform:
                "col_3",
                # Transform method:
                "SET-NULL",
                # Conditions when to transform:
                [
                    {'column': 'col_1', 'equals': "random value"},
                    {'column': 'col_2', 'equals': "passwordHash"},
                ]
            ),

            # Expected output:
            None
        )

        # Not matching condition: Should keep the original value
        self.assertEqual(
            transform.do_transform(
                # Record:
                {"col_1": "random value", "col_2": "id", "col_3": "123456789"},
                # Column to transform:
                "col_3",
                # Transform method:
                "SET-NULL",
                # Conditions when to transform:
                [
                    {'column': 'col_1', 'equals': "random value"},
                    {'column': 'col_2', 'equals': "passwordHash"},
                ]
            ),

            # Expected output:
            "123456789"
        )

    def test_transform_field_in_json_col(self):
        """Test transformation of a field in a json column with no conditions"""

        expected_value = {'id': 1, 'info': {'last_name': 'hidden', 'first_name': 'John'}}

        return_value = transform.do_transform(
            # Record:
            {
                "col_1": "random value",
                "col_2": "passwordHash",
                "col_3": "lkj",
                'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John'}}
            },
            # Column to transform:
            "col_4",
            # Transform method:
            "MASK-HIDDEN",
            # Conditions when to transform:
            None,
            ['info/last_name']
        )

        self.assertDictEqual(expected_value, return_value)

    def test_transform_field_in_json_col_with_conditions(self):
        """Test transformation of a field in a json column with conditions"""

        expected_value = {'id': 1, 'info': {'last_name': 'hidden', 'first_name': 'John'}}

        return_value = transform.do_transform(
            # Record:
            {
                "col_1": "random value",
                "col_2": "passwordHash",
                "col_3": "lkj",
                'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John'}}
            },
            # Column to transform:
            "col_4",
            # Transform method:
            "MASK-HIDDEN",
            # Conditions when to transform:
            [
                {'column': 'col_2', 'equals': "passwordHash"},
            ],
            ['info/last_name']
        )

        self.assertDictEqual(expected_value, return_value)

    def test_transform_fields_in_json_col(self):
        """Test transformation of multiple fields in a json column with no conditions"""

        expected_value = {'id': 1, 'info': {'last_name': 'hidden', 'first_name': 'hidden', 'age': 25}}

        return_value = transform.do_transform(
            # Record:
            {
                "col_1": "random value",
                "col_2": "passwordHash",
                "col_3": "lkj",
                'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'age': 25}}
            },
            # Column to transform:
            "col_4",
            # Transform method:
            "MASK-HIDDEN",
            # Conditions when to transform:
            None,
            ['info/last_name', 'info/first_name']
        )

        self.assertDictEqual(expected_value, return_value)

    def test_transform_col_with_condition_on_json_field(self):
        """Test transformation of a column with condition on a field in a json"""

        record = {
            "col_1": "random value",
            "col_2": "passwordHash",
            "col_3": "323df43983dfs",
            'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'phone': '6573930'}}
        }

        self.assertEqual(
            'hidden',
            transform.do_transform(
                # Record:
                record,
                # Column to transform:
                "col_3",
                # Transform method:
                "MASK-HIDDEN",
                # Conditions when to transform:
                [
                    {'column': 'col_4', 'field_path': 'info/last_name', 'equals': 'Smith'},
                ]
            )
        )

    def test_transform_field_in_json_col_with_condition_on_field(self):
        """Test transformation of a field in a json column with condition on a field in json, condition will be met"""

        record = {
            "col_1": "random value",
            "col_2": "passwordHash",
            "col_3": "lkj",
            'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'phone': '6573930'}}
        }

        self.assertDictEqual(
            {'id': 1, 'info': {'first_name': 'John', 'last_name': None, 'phone': '6573930'}},
            transform.do_transform(
                # Record:
                record,
                # Column to transform:
                "col_4",
                # Transform method:
                "SET-NULL",
                # Conditions when to transform:
                [
                    {'column': 'col_4', 'field_path': 'info/phone', 'equals': '6573930'},
                ],
                ['info/last_name']
            )
        )

    def test_transform_field_in_json_col_with_condition_on_field_2(self):
        """Test transformation of a field in a json column with condition on a field in json,
        the condition will not be met"""

        record = {
            "col_1": "random value",
            "col_2": "passwordHash",
            "col_3": "lkj",
            'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'phone': '6573930'}}
        }

        # not transformed
        self.assertEqual(
            {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'phone': '6573930'}},
            transform.do_transform(
                # Record:
                record,
                # Column to transform:
                "col_4",
                # Transform method:
                "SET-NULL",
                # Conditions when to transform:
                [
                    {'column': 'col_4', 'field_path': 'info/phone', 'regex_match': '.*6573955.*'},
                ],
                ['info/last_name']
            )
        )

    def test_transform_multiple_conditions_all_success(self):
        """Test conditional transformation, all the conditions will be met and transformation should happen"""

        record = {
            "col_1": "random value",
            "col_2": "passwordHash",
            "col_3": "lkj",
            'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'phone': '6573930'}},
            'col_5': '2021-11-30T16:40:07'
        }

        self.assertEqual(
            '2021-01-01T16:40:07',
            transform.do_transform(
                # Record:
                record,
                # Column to transform:
                "col_5",
                # Transform method:
                "MASK-DATE",
                # Conditions when to transform:
                [
                    {'column': 'col_4', 'field_path': 'info/last_name', 'equals': 'Smith'},
                    {'column': 'col_4', 'field_path': 'id', 'equals': 1},
                    {'column': 'col_3', 'regex_match': '.*lkj.*'},
                ]
            )
        )

    def test_transform_multiple_conditions_one_fails(self):
        """Test conditional transformation, one of the conditions will not be met and transformation should not happen"""

        record = {
            "col_1": "random value",
            "col_2": "passwordHash",
            "col_3": "lkj",
            'col_4': {'id': 1, 'info': {'last_name': 'Smith', 'first_name': 'John', 'phone': '6573930'}},
            'col_5': '2021-11-30T16:40:07'
        }

        # not transformed
        self.assertEqual(
            '2021-11-30T16:40:07',
            transform.do_transform(
                # Record:
                record,
                # Column to transform:
                "col_5",
                # Transform method:
                "MASK-DATE",
                # Conditions when to transform:
                [
                    {'column': 'col_4', 'field_path': 'info/last_name', 'equals': 'Smith'},
                    {'column': 'col_4', 'field_path': 'id', 'equals': 2},
                    {'column': 'col_3', 'regex_match': '.*lkj.*'},
                ]
            )
        )

