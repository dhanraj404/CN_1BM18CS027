#Write a program for congestion control using Leaky bucket algorithm.

if __name__ == "__main__":
    storage  = 0 #initial bucket storage 

    #max bucket size 
    bucket_size  = int(input("Enter Max Bucket Capacity: "))
    size_left = bucket_size
    #number of packets going out 
    output_size = int(input("Enter Output Rate::"))
    #number of time buckets content is checked
    queries = int(input("Enter Number of times bucket is checked:"))
    for i in range(queries):
        size_left = bucket_size - storage # space left 
        print("Packet No ", i, ":")
        #number of packets coming in at a time 
        input_size = int(input("Enter Packet Size: "))
        if (input_size <= size_left):
            storage += input_size
            print("Buffer Size = {0} Bucket Size = {1}".format(storage, bucket_size))
            print(input_size, "bytes Sent")
        else:
            print("OverFlow")
            print("Packet Loss = {0} bytes lost".format(input_size-size_left))
            #storage is full 
            storage = bucket_size
            print("Buffer Size = {0} Bucket Size = {1}".format(storage, bucket_size))
        storage -= output_size

