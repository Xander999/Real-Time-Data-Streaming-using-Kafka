
public class KafkaConsumerDemo {

	public static void main(String[] args) {
        SampleConsumer consumerThread = new SampleConsumer("Topic12");
        consumerThread.start();
	}

}
