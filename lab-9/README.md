## 3 Instances

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
