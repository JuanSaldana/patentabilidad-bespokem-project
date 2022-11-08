import time
import django
if __name__=="__main__":
    while True:
        time_uuid = time.time()
        
        #P1 = PLAIN_PATENT(SOURCE_ORIGIN="internal",id=time_uuid,docNumber=f"{time_uuid}")
        #print(f"created PLAIN_PATENT:{P1}")
        print(f"{time_uuid}")
        time.sleep(1)