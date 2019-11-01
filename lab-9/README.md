## Before turning primary node off

### rs.status()
```
rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T20:50:12.185Z"),
	"myState" : 2,
	"term" : NumberLong(1),
	"syncingTo" : "instance-2:27017",
	"syncSourceHost" : "instance-2:27017",
	"syncSourceId" : 1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572641406, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T20:50:06.836Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572641406, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T20:50:06.836Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572641406, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572641406, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T20:50:06.836Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T20:50:06.836Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572641406, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572641406, 1),
	"members" : [
		{
			"_id" : 0,
			"name" : "instance-1:27017",
			"ip" : "172.31.35.225",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 796,
			"optime" : {
				"ts" : Timestamp(1572641406, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572641406, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:50:06Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:50:06Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:50:11.658Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:50:11.658Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "instance-2:27017",
			"syncSourceHost" : "instance-2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 1,
			"name" : "instance-2:27017",
			"ip" : "172.31.33.185",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 796,
			"optime" : {
				"ts" : Timestamp(1572641406, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572641406, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:50:06Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:50:06Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:50:11.659Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:50:10.744Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572640626, 1),
			"electionDate" : ISODate("2019-11-01T20:37:06Z"),
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "instance-3:27017",
			"ip" : "172.31.44.137",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 806,
			"optime" : {
				"ts" : Timestamp(1572641406, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:50:06Z"),
			"syncingTo" : "instance-2:27017",
			"syncSourceHost" : "instance-2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572641406, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572641406, 1)
}
```

### rs.conf()
```
rs.conf()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "instance-1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "instance-2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "instance-3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbc97678498361811258697")
	}
}
```

## After turning primry node off
### rs.status()
```
rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T21:10:40.700Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572642639, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T21:10:39.848Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572642639, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T21:10:39.848Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572642639, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572642639, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T21:10:39.848Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T21:10:39.848Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572642608, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572642608, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-11-01T21:08:59.002Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572642536, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572642536, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 1,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T21:08:59.844Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T21:09:01.067Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "instance-1:27017",
			"ip" : "172.31.35.225",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 2623,
			"optime" : {
				"ts" : Timestamp(1572642639, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T21:10:39Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "could not find member to sync from",
			"electionTime" : Timestamp(1572642539, 1),
			"electionDate" : ISODate("2019-11-01T21:08:59Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "instance-2:27017",
			"ip" : "172.31.33.185",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-11-01T21:10:31.917Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T21:08:58.911Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to instance-2:27017 (172.31.33.185:27017) :: caused by :: No route to host",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 2,
			"name" : "instance-3:27017",
			"ip" : "172.31.44.137",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 2024,
			"optime" : {
				"ts" : Timestamp(1572642629, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572642629, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T21:10:29Z"),
			"optimeDurableDate" : ISODate("2019-11-01T21:10:29Z"),
			"lastHeartbeat" : ISODate("2019-11-01T21:10:39.018Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T21:10:39.066Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "instance-1:27017",
			"syncSourceHost" : "instance-1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572642639, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572642639, 1)
}
```

### rs.conf()
```
rs.conf()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "instance-1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "instance-2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "instance-3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbc97678498361811258697")
	}
}
```