
public class KafkaProducerDemo {

	public static final String TOPIC = "testTopic";
	
	public static void main(String[] args) {
		boolean isAsync = false;
        SimpleProducer producerThread = new SimpleProducer(TOPIC, isAsync);
        // start the producer
        producerThread.start();
 	}

}
