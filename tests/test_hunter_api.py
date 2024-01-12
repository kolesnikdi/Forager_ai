from hunter_api.classes import HunterClient

api_key = '5022aaa4abd272d308b04f687fadeaf0aeb0af82'
run_email_finder = HunterClient('email_verifier', api_key)
instance = run_email_finder.instance
instance.create('kolesnik.d.i@gmail.com')
received_data = instance.read('kolesnik.d.i@gmail.com')
instance.update('kolesnik.d.i@gmail.com', 'segareta@ukr.net')
instance.delete('segareta@ukr.net')
