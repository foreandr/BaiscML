#slightly altered code from   https://github.com/minimaxir/gpt-2-simple
 # NOT WORKING
import gpt_2_simple as gpt2
model_name = "124M"
# model is saved into current directory under /models/124M/
#gpt2.download_gpt2(model_name=model_name) #need to run only once. comment out once done.
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
gpt2.generate(sess)
gpt2.generate(sess, length=39, include_prefix=False, temperature=0.1, top_k=1, top_p=0.9,
              run_name='run1', prefix="Is there Earth No.2?", return_as_list=True)