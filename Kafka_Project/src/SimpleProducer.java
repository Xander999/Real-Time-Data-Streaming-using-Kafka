import org.apache.kafka.clients.producer.Callback;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;
import java.util.concurrent.ExecutionException;
 

//Read from database and Publish it in a Topic on Kafka


public class SimpleProducer extends Thread {
    private final KafkaProducer<Integer, String> producer;
    private final String topic;
    private final Boolean isAsync;
 
    public static final String KAFKA_SERVER_URL = "localhost";
    public static final int KAFKA_SERVER_PORT = 19092;
    public static final String CLIENT_ID = "SimpleProducer";
 
    public SimpleProducer(String topic, Boolean isAsync) {
        Properties properties = new Properties();
        properties.put("bootstrap.servers", KAFKA_SERVER_URL + ":" + KAFKA_SERVER_PORT);
        properties.put("client.id", CLIENT_ID);
        properties.put("key.serializer", "org.apache.kafka.common.serialization.IntegerSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        producer = new KafkaProducer<>(properties);
        this.topic = topic;
        this.isAsync = isAsync;
    }
 
    public void run() {
       /* int messageNo = 1;
        while (messageNo<10) {
            String messageStr = "Message_" + messageNo;
            long startTime = System.currentTimeMillis();
            if (isAsync) { // Send asynchronously
                producer.send(new ProducerRecord<>(topic, messageNo, messageStr), new DemoCallBack(startTime, messageNo, messageStr));
            } 
            else { // Send synchronously
                try {
                    producer.send(new ProducerRecord<>(topic, messageNo, messageStr)).get();
                    System.out.println("Sent message: (" + messageNo + ", " + messageStr + ")");
                } catch (InterruptedException | ExecutionException e) {
                    e.printStackTrace();
                    // handle the exception
                }
            }
            ++messageNo;
        }  */
    	
    	int messageNo=1;
    	
    	try {
    		Class.forName("com.mysql.jdbc.Driver");
    		   Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/exp?useSSL=false", "XANDER","xander21");
    		   Statement mystatement = con.createStatement();
    		   ResultSet codespeedy=mystatement.executeQuery("select * from employee");
    		      while(codespeedy.next())
    		      {
    		    	  String messageStr=codespeedy.getInt("eid")+"  "+codespeedy.getString("ename")+"  "+codespeedy.getInt("esal")+" "+codespeedy.getString("edep");
    		          System.out.println(codespeedy.getInt("eid")+"  "+codespeedy.getString("ename")+"  "+codespeedy.getInt("esal")+" "+codespeedy.getString("edep"));  
    		          producer.send(new ProducerRecord<>(topic, messageNo, messageStr)).get();
    		          messageNo++;
    		      }
    		      
    		         }   
    		         catch (Exception e){
    		     System.out.println(e);
    		    }
    	
    }
}
 
class DemoCallBack implements Callback {
 
    private final long startTime;
    private final int key;
    private final String message;
 
    public DemoCallBack(long startTime, int key, String message) {
        this.startTime = startTime;
        this.key = key;
        this.message = message;
    }
 
    /**
     * onCompletion method will be called when the record sent to the Kafka Server has been acknowledged.
     *
     * @param metadata  The metadata contains the partition and offset of the record. Null if an error occurred.
     * @param exception The exception thrown during processing of this record. Null if no error occurred.
     */
    public void onCompletion(RecordMetadata metadata, Exception exception) {
        long elapsedTime = System.currentTimeMillis() - startTime;
        if (metadata != null) {
            System.out.println(
                    "message(" + key + ", " + message + ") sent to partition(" + metadata.partition() +
                    "), " +
                    "offset(" + metadata.offset() + ") in " + elapsedTime + " ms");
        } else {
            exception.printStackTrace();
        }
    }
}
