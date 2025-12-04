# tv_show.py file
# main program
import tv

def main():
   # object creation
   my_tv = tv.TV()

   # object usage
   my_tv.show_status()
   my_tv.turn_on()
   my_tv.show_status()
   my_tv.turn_off()
   my_tv.show_status()

if __name__ == "__main__":
   main() 