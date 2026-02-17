from promise import Promise


def fulfilled_promise(result=None):
  
  def make_promise(resolve, reject):
    resolve(result)

  return Promise(make_promise)