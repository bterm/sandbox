#include <string.h>
#include <exception>

#include "scribe_utils.h"

#include <protocol/TBinaryProtocol.h>
#include <transport/TSocket.h>
#include <transport/TTransportUtils.h>

#include "gen-cpp/scribe.h"

using namespace std;
using std::string;
using boost::shared_ptr;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
using namespace apache::thrift;
using namespace scribe::thrift;
using namespace scribe;

int scribe_open(scribe_t *p, const char *host, const int port)
{
	p->host = strdup(host);
	p->port = port;
	
	shared_ptr<TTransport> socket(new TSocket(p->host, p->port));
	shared_ptr<TTransport> transport(new TFramedTransport(socket));
	shared_ptr<TProtocol>  protocol(new TBinaryProtocol(transport));
	
	scribeClient *client = new scribeClient(protocol);
	
	try 
	{
		transport->open();
		p->scribeClient = client;
		p->transport    = static_cast<void*>(transport.get());
	} 
	catch (TException &tx) 
	{
		return 1;
	}
		
	return 0;
}

int scribe_write(scribe_t *p, const char *category, const char *buf)
{
	LogEntry entry;
	entry.category = category;
	entry.message = buf;
	
	std::vector<LogEntry> msgs;
	msgs.push_back(entry);
	
	int result = ((scribeClient*)p->scribeClient)->Log(msgs);
	return result;
}

int scribe_close(scribe_t *p)
{
	((TTransport*)p->transport)->close();
	delete (scribeClient*)p->scribeClient;
	memset(p, 0, sizeof(scribe_t));
	return 0;
}


int scribe_send_msg(char* host, unsigned long port, char* category, char* msg)
{
	int result = 1;
	
	// check to see if there is a new line at the end of the msg, if not add one
	try {
		char message[4096];
		char* p = strchr(msg,'\n');
		
		if (p)
		{
			sprintf(message, "%s", msg);	
		}
		else 
		{
			sprintf(message, "%s\n", msg);	
		}
		
		scribe_t *scribe = (scribe_t*) calloc(1, sizeof(scribe_t));
		scribe_open(scribe, host, port);
		result = scribe_write(scribe, category, message);
		scribe_close(scribe);
	}  catch(exception& e) {
		result = 1;
	}
		
	return result;
}

