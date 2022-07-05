

def start_transcribe_job(video_id, input_format):
    """

    :param video_id:
    :param input_format: ['mp3' | 'mp4' | 'wav' | 'flac' | 'ogg' | 'amr' | 'webm']
    :return:
    """
    response = client.start_transcription_job(
        TranscriptionJobName='string',
        MediaFormat=input_format,
        Media={
            'MediaFileUri': 'string',
            'RedactedMediaFileUri': 'string'
        },
        OutputBucketName='string',
        OutputKey='string',
        OutputEncryptionKMSKeyId='string',
        KMSEncryptionContext={
            'string': 'string'
        },
        Settings={
            'VocabularyName': 'string',
            'ShowSpeakerLabels': True | False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True | False,
            'ShowAlternatives': True | False,
            'MaxAlternatives': 123,
            'VocabularyFilterName': 'string',
            'VocabularyFilterMethod': 'remove' | 'mask' | 'tag'
        },
        ModelSettings={
            'LanguageModelName': 'string'
        },
        JobExecutionSettings={
            'AllowDeferredExecution': True | False,
            'DataAccessRoleArn': 'string'
        },
        ContentRedaction={
            'RedactionType': 'PII',
            'RedactionOutput': 'redacted' | 'redacted_and_unredacted',
            'PiiEntityTypes': [
                'BANK_ACCOUNT_NUMBER' | 'BANK_ROUTING' | 'CREDIT_DEBIT_NUMBER' | 'CREDIT_DEBIT_CVV' |
                'CREDIT_DEBIT_EXPIRY' | 'PIN' | 'EMAIL' | 'ADDRESS' | 'NAME' | 'PHONE' | 'SSN' | 'ALL',
            ]
        },
        IdentifyLanguage=True | False,
        LanguageOptions=[
            'af-ZA' | 'ar-AE' | 'ar-SA' | 'cy-GB' | 'da-DK' | 'de-CH' | 'de-DE' | 'en-AB' | 'en-AU' | 'en-GB' |
            'en-IE' | 'en-IN' | 'en-US' | 'en-WL' | 'es-ES' | 'es-US' | 'fa-IR' | 'fr-CA' | 'fr-FR' | 'ga-IE' |
            'gd-GB' | 'he-IL' | 'hi-IN' | 'id-ID' | 'it-IT' | 'ja-JP' | 'ko-KR' | 'ms-MY' | 'nl-NL' | 'pt-BR' |
            'pt-PT' | 'ru-RU' | 'ta-IN' | 'te-IN' | 'tr-TR' | 'zh-CN' | 'zh-TW' | 'th-TH' | 'en-ZA' | 'en-NZ',
        ],
        Subtitles={
            'Formats': [
                'vtt' | 'srt',
            ],
            'OutputStartIndex': 123
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        LanguageIdSettings={
            'string': {
                'VocabularyName': 'string',
                'VocabularyFilterName': 'string',
                'LanguageModelName': 'string'
            }
        }
    )