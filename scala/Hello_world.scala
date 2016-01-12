

object Hello_world extends App {
  
  
   val c = caseEX("Praveen", "A")
  
  val y =  xx 
  apply("P","A") //or xx()
  
  print (c +"\n"+ y)
   
}

  case class caseEX(firstName: String, lastName: String)
  
  
  
  
  
  
  
  
  
  
  
  
  
  class xx( fn1: String,  ln1:String)  {
    
    def firstName = fn1
    def lastName = ln1
  
 override def toString() = {
   
   "xx("+firstName+", "+lastName+")"
  
  }
  
  }
  
  object xx{
    
    def apply(fn:String, ln:String):xx = new xx(fn, ln)
    
    def unapply() = {
      
    }
    
    
  }
 
  
 

