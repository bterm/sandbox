/**
 *  SQLite wrapper   
 *  Based on sqlite wrapper by Matteo Bertozzi.
 *
 *	Requires:
 *		import libsqlite3.0.dylib
 *		Add > Existing Frameworks... change dropdown to dylibs and select 'libsqlite3.0.dylib' 
 *
 *	Usage:
 *		Sqlite *sqlite = [[Sqlite alloc] init];
 *
 *		if (![sqlite open:@"sample.db"])
 *			return;
 *
 *		[sqlite executeNonQuery:@"DROP TABLE test"];
 *		[sqlite executeNonQuery:@"CREATE TABLE test (key TEXT NOT NULL, num INTEGER, value TEXT);"];
 *		[sqlite executeNonQuery:@"INSERT INTO test VALUES (?, ?, ?);", [Sqlite createUuid], [NSNumber numberWithInt:5], @"example"];
 *		[sqlite executeNonQuery:@"INSERT INTO test VALUES (?, ?, ?);", [Sqlite createUuid], [NSNumber numberWithInt:3], @"values"];
 *
 *		NSArray *results = [sqlite executeQuery:@"SELECT * FROM test;"];
 *
 *		for (NSDictionary *dictionary in results) {
 *			for (NSString *key in [dictionary keyEnumerator])
 *				NSLog(@"%@ %@\n", key, [dictionary objectForKey:key]]);
 *			}
 *		}
 *		
 *		[results release];
 *		[sqlite release];
 *
 **/
#import <Foundation/Foundation.h>
#import <sqlite3.h>

@interface Sqlite : NSObject {
	NSInteger busyRetryTimeout;
	NSString *filePath;
	sqlite3 *_db;
}

@property (readwrite) NSInteger busyRetryTimeout;
@property (readonly) NSString *filePath;

+ (NSString *)createUuid;
+ (NSString *)version;

- (id)initWithFile:(NSString *)filePath;

- (BOOL)open:(NSString *)filePath;
- (void)close;

- (NSInteger)errorCode;
- (NSString *)errorMessage;

- (NSArray *)executeQuery:(NSString *)sql, ...;
- (NSArray *)executeQuery:(NSString *)sql arguments:(NSArray *)args;

- (BOOL)executeNonQuery:(NSString *)sql, ...;
- (BOOL)executeNonQuery:(NSString *)sql arguments:(NSArray *)args;

- (BOOL)commit;
- (BOOL)rollback;
- (BOOL)beginTransaction;
- (BOOL)beginDeferredTransaction;

@end

