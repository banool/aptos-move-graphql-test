from typing import Any, List, TypedDict


## Scalars

Address = str

Any = Any

U128 = str

U16 = int

U256 = str

U32 = int

U64 = str

U8 = int

ACL = TypedDict('ACL', {
	'list': List['Address'],
})


AUID = TypedDict('AUID', {
	'unique_address': 'Address',
})


Account = TypedDict('Account', {
	'authentication_key': List['U8'],
	'sequence_number': 'U64',
	'guid_creation_num': 'U64',
	'coin_register_events': 'EventHandle',
	'key_rotation_events': 'EventHandle',
	'rotation_capability_offer': 'CapabilityOffer',
	'signer_capability_offer': 'CapabilityOffer',
})


AccountMap = TypedDict('AccountMap', {
	'account_address': 'Address',
	'balance': 'U64',
})


AddDistributionEvent = TypedDict('AddDistributionEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
	'amount': 'U64',
})


AddOwnersEvent = TypedDict('AddOwnersEvent', {
	'owners_added': List['Address'],
})


AdminStore = TypedDict('AdminStore', {
	'vesting_contracts': List['Address'],
	'nonce': 'U64',
	'create_events': 'EventHandle',
})


AdminWithdrawEvent = TypedDict('AdminWithdrawEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'amount': 'U64',
})


AestheticProfile = TypedDict('AestheticProfile', {
	'color': 'Color',
	'texture': str,
})


AggrOrMultiSignature = TypedDict('AggrOrMultiSignature', {
	'bytes': List['U8'],
})


AggrPublicKeysWithPoP = TypedDict('AggrPublicKeysWithPoP', {
	'bytes': List['U8'],
})


AggregatableCoin = TypedDict('AggregatableCoin', {
	'value': 'Aggregator',
})


Aggregator = TypedDict('Aggregator', {
	'handle': 'Address',
	'key': 'Address',
	'limit': 'U128',
})


AggregatorFactory = TypedDict('AggregatorFactory', {
	'phantom_table': 'Table',
})


AllowedDep = TypedDict('AllowedDep', {
	'account': 'Address',
	'module_name': str,
})


AllowedValidators = TypedDict('AllowedValidators', {
	'accounts': List['Address'],
})


ApprovedExecutionHashes = TypedDict('ApprovedExecutionHashes', {
	'hashes': 'SimpleMap',
})


AptosCoin = TypedDict('AptosCoin', {
	'dummy_field': bool,
})


BigVector = TypedDict('BigVector', {
	'buckets': 'TableWithLength',
	'end_index': 'U64',
	'bucket_size': 'U64',
})


BitVector = TypedDict('BitVector', {
	'length': 'U64',
	'bit_field': List[bool],
})


BlockResource = TypedDict('BlockResource', {
	'height': 'U64',
	'epoch_interval': 'U64',
	'new_block_events': 'EventHandle',
	'update_epoch_interval_events': 'EventHandle',
})


Box = TypedDict('Box', {
	'val': 'Any',
})


BurnCapability = TypedDict('BurnCapability', {
	'dummy_field': bool,
})


BurnRef = TypedDict('BurnRef', {
	'metadata': 'Object',
})


Cap = TypedDict('Cap', {
	'root': 'Address',
})


CapDelegateState = TypedDict('CapDelegateState', {
	'root': 'Address',
})


CapState = TypedDict('CapState', {
	'delegates': List['Address'],
})


Capabilities = TypedDict('Capabilities', {
	'burn_cap': 'BurnCapability',
	'freeze_cap': 'FreezeCapability',
	'mint_cap': 'MintCapability',
})


CapabilityOffer = TypedDict('CapabilityOffer', {
	'for': 'Option',
})


ChainId = TypedDict('ChainId', {
	'id': 'U8',
})


Ciphertext = TypedDict('Ciphertext', {
	'left': 'RistrettoPoint',
	'right': 'RistrettoPoint',
})


Coin = TypedDict('Coin', {
	'value': 'U64',
})


CoinInfo = TypedDict('CoinInfo', {
	'name': str,
	'symbol': str,
	'decimals': 'U8',
	'supply': 'Option',
})


CoinRegisterEvent = TypedDict('CoinRegisterEvent', {
	'type_info': 'TypeInfo',
})


CoinStore = TypedDict('CoinStore', {
	'coin': 'Coin',
	'frozen': bool,
	'deposit_events': 'EventHandle',
	'withdraw_events': 'EventHandle',
})


CollectedFeesPerBlock = TypedDict('CollectedFeesPerBlock', {
	'amount': 'AggregatableCoin',
	'proposer': 'Option',
	'burn_percentage': 'U8',
})


Color = TypedDict('Color', {
	'r': 'U8',
	'g': 'U8',
	'b': 'U8',
})


Commitment = TypedDict('Commitment', {
	'point': 'RistrettoPoint',
})


CompressedCiphertext = TypedDict('CompressedCiphertext', {
	'left': 'CompressedRistretto',
	'right': 'CompressedRistretto',
})


CompressedPubkey = TypedDict('CompressedPubkey', {
	'point': 'CompressedRistretto',
})


CompressedRistretto = TypedDict('CompressedRistretto', {
	'data': List['U8'],
})


Configuration = TypedDict('Configuration', {
	'epoch': 'U64',
	'last_reconfiguration_time': 'U64',
	'events': 'EventHandle',
})


Cons = TypedDict('Cons', {
	'car': 'Any',
	'cdr': 'Any',
})


ConsensusConfig = TypedDict('ConsensusConfig', {
	'config': List['U8'],
})


ConstructorRef = TypedDict('ConstructorRef', {
	'self': 'Address',
	'can_delete': bool,
})


Container = TypedDict('Container', {
	'store': 'SimpleMap',
})


CreateStakingContractEvent = TypedDict('CreateStakingContractEvent', {
	'operator': 'Address',
	'voter': 'Address',
	'pool_address': 'Address',
	'principal': 'U64',
	'commission_percentage': 'U64',
})


CreateTransactionEvent = TypedDict('CreateTransactionEvent', {
	'creator': 'Address',
	'sequence_number': 'U64',
	'transaction': 'MultisigTransaction',
})


CreateVestingContractEvent = TypedDict('CreateVestingContractEvent', {
	'operator': 'Address',
	'voter': 'Address',
	'grant_amount': 'U64',
	'withdrawal_address': 'Address',
	'vesting_contract_address': 'Address',
	'staking_pool_address': 'Address',
	'commission_percentage': 'U64',
})


CurrentTimeMicroseconds = TypedDict('CurrentTimeMicroseconds', {
	'microseconds': 'U64',
})


DelegateVotingPowerEvent = TypedDict('DelegateVotingPowerEvent', {
	'pool_address': 'Address',
	'delegator': 'Address',
	'voter': 'Address',
})


DelegatedMintCapability = TypedDict('DelegatedMintCapability', {
	'to': 'Address',
})


DelegatedVotes = TypedDict('DelegatedVotes', {
	'active_shares': 'U128',
	'pending_inactive_shares': 'U128',
	'active_shares_next_lockup': 'U128',
	'last_locked_until_secs': 'U64',
})


DelegationPool = TypedDict('DelegationPool', {
	'active_shares': '_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64_unbound__Pool',
	'observed_lockup_cycle': 'ObservedLockupCycle',
	'inactive_shares': 'Table',
	'pending_withdrawals': 'Table',
	'stake_pool_signer_cap': 'SignerCapability',
	'total_coins_inactive': 'U64',
	'operator_commission_percentage': 'U64',
	'add_stake_events': 'EventHandle',
	'reactivate_stake_events': 'EventHandle',
	'unlock_stake_events': 'EventHandle',
	'withdraw_stake_events': 'EventHandle',
	'distribute_commission_events': 'EventHandle',
})


DelegationPoolOwnership = TypedDict('DelegationPoolOwnership', {
	'pool_address': 'Address',
})


Delegations = TypedDict('Delegations', {
	'inner': List['DelegatedMintCapability'],
})


DeleteRef = TypedDict('DeleteRef', {
	'self': 'Address',
})


DeriveRef = TypedDict('DeriveRef', {
	'self': 'Address',
})


DeriveRefPod = TypedDict('DeriveRefPod', {
	'metadata_derive_ref': 'DeriveRef',
})


DirectCoinTransferConfigUpdatedEvent = TypedDict('DirectCoinTransferConfigUpdatedEvent', {
	'new_allow_direct_transfers': bool,
})


DirectTransferConfig = TypedDict('DirectTransferConfig', {
	'allow_arbitrary_coin_transfers': bool,
	'update_coin_transfer_events': 'EventHandle',
})


DisableReconfiguration = TypedDict('DisableReconfiguration', {
	'dummy_field': bool,
})


DistributeCommissionEvent = TypedDict('DistributeCommissionEvent', {
	'pool_address': 'Address',
	'operator': 'Address',
	'commission_active': 'U64',
	'commission_pending_inactive': 'U64',
})


DistributeRewardsEvent = TypedDict('DistributeRewardsEvent', {
	'pool_address': 'Address',
	'rewards_amount': 'U64',
})


ECDSARawPublicKey = TypedDict('ECDSARawPublicKey', {
	'bytes': List['U8'],
})


ECDSASignature = TypedDict('ECDSASignature', {
	'bytes': List['U8'],
})


EmployeeAccountMap = TypedDict('EmployeeAccountMap', {
	'accounts': List['Address'],
	'validator': 'ValidatorConfigurationWithCommission',
	'vesting_schedule_numerator': List['U64'],
	'vesting_schedule_denominator': 'U64',
	'beneficiary_resetter': 'Address',
})


Entry = TypedDict('Entry', {
	'hash': 'U64',
	'key': 'Any',
	'value': 'Any',
})


EventHandle = TypedDict('EventHandle', {
	'counter': 'U64',
	'guid': 'GUID',
})


ExecuteRejectedTransactionEvent = TypedDict('ExecuteRejectedTransactionEvent', {
	'sequence_number': 'U64',
	'num_rejections': 'U64',
	'executor': 'Address',
})


ExecutionConfig = TypedDict('ExecutionConfig', {
	'config': List['U8'],
})


ExecutionError = TypedDict('ExecutionError', {
	'abort_location': str,
	'error_type': str,
	'error_code': 'U64',
})


ExtendRef = TypedDict('ExtendRef', {
	'self': 'Address',
})


FakeCons = TypedDict('FakeCons', {
	'car': 'Any',
	'cdr': 'Any',
})


Features = TypedDict('Features', {
	'features': List['U8'],
})


FixedPoint32 = TypedDict('FixedPoint32', {
	'value': 'U64',
})


FixedPoint64 = TypedDict('FixedPoint64', {
	'value': 'U128',
})


FormatFq12LscLsb = TypedDict('FormatFq12LscLsb', {
	'dummy_field': bool,
})


FormatFrLsb = TypedDict('FormatFrLsb', {
	'dummy_field': bool,
})


FormatFrMsb = TypedDict('FormatFrMsb', {
	'dummy_field': bool,
})


FormatG1Compr = TypedDict('FormatG1Compr', {
	'dummy_field': bool,
})


FormatG1Uncompr = TypedDict('FormatG1Uncompr', {
	'dummy_field': bool,
})


FormatG2Compr = TypedDict('FormatG2Compr', {
	'dummy_field': bool,
})


FormatG2Uncompr = TypedDict('FormatG2Uncompr', {
	'dummy_field': bool,
})


FormatGt = TypedDict('FormatGt', {
	'dummy_field': bool,
})


Fq12 = TypedDict('Fq12', {
	'dummy_field': bool,
})


Fr = TypedDict('Fr', {
	'dummy_field': bool,
})


FreezeCapability = TypedDict('FreezeCapability', {
	'dummy_field': bool,
})


FrozenEvent = TypedDict('FrozenEvent', {
	'frozen': bool,
})


FungibleAsset = TypedDict('FungibleAsset', {
	'metadata': 'Object',
	'amount': 'U64',
})


FungibleAssetEvents = TypedDict('FungibleAssetEvents', {
	'deposit_events': 'EventHandle',
	'withdraw_events': 'EventHandle',
	'frozen_events': 'EventHandle',
})


FungibleStore = TypedDict('FungibleStore', {
	'metadata': 'Object',
	'balance': 'U64',
	'frozen': bool,
})


G1 = TypedDict('G1', {
	'dummy_field': bool,
})


G2 = TypedDict('G2', {
	'dummy_field': bool,
})


GUID = TypedDict('GUID', {
	'id': '_0x0000000000000000000000000000000000000000000000000000000000000001__guid__ID',
})


GasCurve = TypedDict('GasCurve', {
	'min_gas': 'U64',
	'max_gas': 'U64',
	'points': List['Point'],
})


GasEntry = TypedDict('GasEntry', {
	'key': str,
	'val': 'U64',
})


GasParameter = TypedDict('GasParameter', {
	'usage': 'Usage',
})


GasSchedule = TypedDict('GasSchedule', {
	'entries': List['GasEntry'],
})


GasScheduleV2 = TypedDict('GasScheduleV2', {
	'feature_version': 'U64',
	'entries': List['GasEntry'],
})


GenesisEndMarker = TypedDict('GenesisEndMarker', {
	'dummy_field': bool,
})


GovernanceConfig = TypedDict('GovernanceConfig', {
	'min_voting_threshold': 'U128',
	'required_proposer_stake': 'U64',
	'voting_duration_secs': 'U64',
})


GovernanceEvents = TypedDict('GovernanceEvents', {
	'create_proposal_events': 'EventHandle',
	'update_config_events': 'EventHandle',
	'vote_events': 'EventHandle',
})


GovernanceProposal = TypedDict('GovernanceProposal', {
	'dummy_field': bool,
})


GovernanceRecords = TypedDict('GovernanceRecords', {
	'votes': 'SmartTable',
	'votes_per_proposal': 'SmartTable',
	'vote_delegation': 'SmartTable',
	'delegated_votes': 'SmartTable',
	'vote_events': 'EventHandle',
	'create_proposal_events': 'EventHandle',
	'delegate_voting_power_events': 'EventHandle',
})


GovernanceResponsbility = TypedDict('GovernanceResponsbility', {
	'signer_caps': 'SimpleMap',
})


Gt = TypedDict('Gt', {
	'dummy_field': bool,
})


HashG1XmdSha256SswuRo = TypedDict('HashG1XmdSha256SswuRo', {
	'dummy_field': bool,
})


HashG2XmdSha256SswuRo = TypedDict('HashG2XmdSha256SswuRo', {
	'dummy_field': bool,
})


IncreaseLockupEvent = TypedDict('IncreaseLockupEvent', {
	'pool_address': 'Address',
	'old_locked_until_secs': 'U64',
	'new_locked_until_secs': 'U64',
})


IndividualValidatorPerformance = TypedDict('IndividualValidatorPerformance', {
	'successful_proposals': 'U64',
	'failed_proposals': 'U64',
})


Integer = TypedDict('Integer', {
	'value': 'U128',
	'limit': 'U128',
})


JoinValidatorSetEvent = TypedDict('JoinValidatorSetEvent', {
	'pool_address': 'Address',
})


KeyRotationEvent = TypedDict('KeyRotationEvent', {
	'old_authentication_key': List['U8'],
	'new_authentication_key': List['U8'],
})


LeaveValidatorSetEvent = TypedDict('LeaveValidatorSetEvent', {
	'pool_address': 'Address',
})


LinearCap = TypedDict('LinearCap', {
	'root': 'Address',
})


LinearTransferRef = TypedDict('LinearTransferRef', {
	'self': 'Address',
	'owner': 'Address',
})


Meal = TypedDict('Meal', {
	'name': str,
	'protein': 'Option',
	'vegetables': List['Object'],
	'cost_usd': 'U32',
	'popularity_by_country': 'SimpleMap',
})


MealStore = TypedDict('MealStore', {
	'meals': List['Object'],
})


Metadata = TypedDict('Metadata', {
	'name': str,
	'symbol': str,
	'decimals': 'U8',
	'icon_uri': str,
	'project_uri': str,
})


MetadataUpdatedEvent = TypedDict('MetadataUpdatedEvent', {
	'old_metadata': 'SimpleMap',
	'new_metadata': 'SimpleMap',
})


MintCapStore = TypedDict('MintCapStore', {
	'mint_cap': 'MintCapability',
})


MintCapability = TypedDict('MintCapability', {
	'dummy_field': bool,
})


MintRef = TypedDict('MintRef', {
	'metadata': 'Object',
})


ModuleMetadata = TypedDict('ModuleMetadata', {
	'name': str,
	'source': List['U8'],
	'source_map': List['U8'],
	'extension': 'Option',
})


MultisigAccount = TypedDict('MultisigAccount', {
	'owners': List['Address'],
	'num_signatures_required': 'U64',
	'transactions': 'Table',
	'last_executed_sequence_number': 'U64',
	'next_sequence_number': 'U64',
	'signer_cap': 'Option',
	'metadata': 'SimpleMap',
	'add_owners_events': 'EventHandle',
	'remove_owners_events': 'EventHandle',
	'update_signature_required_events': 'EventHandle',
	'create_transaction_events': 'EventHandle',
	'vote_events': 'EventHandle',
	'execute_rejected_transaction_events': 'EventHandle',
	'execute_transaction_events': 'EventHandle',
	'transaction_execution_failed_events': 'EventHandle',
	'metadata_updated_events': 'EventHandle',
})


MultisigAccountCreationMessage = TypedDict('MultisigAccountCreationMessage', {
	'chain_id': 'U8',
	'account_address': 'Address',
	'sequence_number': 'U64',
	'owners': List['Address'],
	'num_signatures_required': 'U64',
})


MultisigAccountCreationWithAuthKeyRevocationMessage = TypedDict('MultisigAccountCreationWithAuthKeyRevocationMessage', {
	'chain_id': 'U8',
	'account_address': 'Address',
	'sequence_number': 'U64',
	'owners': List['Address'],
	'num_signatures_required': 'U64',
})


MultisigTransaction = TypedDict('MultisigTransaction', {
	'payload': 'Option',
	'payload_hash': 'Option',
	'votes': 'SimpleMap',
	'creator': 'Address',
	'creation_time_secs': 'U64',
})


NIL = TypedDict('NIL', {
	'dummy_field': bool,
})


NewBlockEvent = TypedDict('NewBlockEvent', {
	'hash': 'Address',
	'epoch': 'U64',
	'round': 'U64',
	'height': 'U64',
	'previous_block_votes_bitvec': List['U8'],
	'proposer': 'Address',
	'failed_proposer_indices': List['U64'],
	'time_microseconds': 'U64',
})


NewEpochEvent = TypedDict('NewEpochEvent', {
	'epoch': 'U64',
})


Object = TypedDict('Object', {
	'inner': 'Address',
})


ObjectCore = TypedDict('ObjectCore', {
	'guid_creation_num': 'U64',
	'owner': 'Address',
	'allow_ungated_transfer': bool,
	'transfer_events': 'EventHandle',
})


ObjectGroup = TypedDict('ObjectGroup', {
	'dummy_field': bool,
})


ObservedLockupCycle = TypedDict('ObservedLockupCycle', {
	'index': 'U64',
})


Option = TypedDict('Option', {
	'vec': List['Any'],
})


OptionalAggregator = TypedDict('OptionalAggregator', {
	'aggregator': 'Option',
	'integer': 'Option',
})


OriginatingAddress = TypedDict('OriginatingAddress', {
	'address_map': 'Table',
})


OwnerCapability = TypedDict('OwnerCapability', {
	'pool_address': 'Address',
})


PackageDep = TypedDict('PackageDep', {
	'account': 'Address',
	'package_name': str,
})


PackageMetadata = TypedDict('PackageMetadata', {
	'name': str,
	'upgrade_policy': 'UpgradePolicy',
	'upgrade_number': 'U64',
	'source_digest': str,
	'manifest': List['U8'],
	'modules': List['ModuleMetadata'],
	'deps': List['PackageDep'],
	'extension': 'Option',
})


PackageRegistry = TypedDict('PackageRegistry', {
	'packages': List['PackageMetadata'],
})


Point = TypedDict('Point', {
	'x': 'U64',
	'y': 'U64',
})


ProofOfPossession = TypedDict('ProofOfPossession', {
	'bytes': List['U8'],
})


Proposal = TypedDict('Proposal', {
	'proposer': 'Address',
	'execution_content': 'Option',
	'metadata': 'SimpleMap',
	'creation_time_secs': 'U64',
	'execution_hash': List['U8'],
	'min_vote_threshold': 'U128',
	'expiration_secs': 'U64',
	'early_resolution_vote_threshold': 'Option',
	'yes_votes': 'U128',
	'no_votes': 'U128',
	'is_resolved': bool,
	'resolution_time_secs': 'U64',
})


Protein = TypedDict('Protein', {
	'name': str,
	'energy_joules': 'U64',
	'aesthetic_profile': 'AestheticProfile',
})


PublicKey = TypedDict('PublicKey', {
	'bytes': List['U8'],
})


PublicKeyWithPoP = TypedDict('PublicKeyWithPoP', {
	'bytes': List['U8'],
})


RangeProof = TypedDict('RangeProof', {
	'bytes': List['U8'],
})


RecordKey = TypedDict('RecordKey', {
	'stake_pool': 'Address',
	'proposal_id': 'U64',
})


RegisterForumEvent = TypedDict('RegisterForumEvent', {
	'hosting_account': 'Address',
	'proposal_type_info': 'TypeInfo',
})


RegisterValidatorCandidateEvent = TypedDict('RegisterValidatorCandidateEvent', {
	'pool_address': 'Address',
})


RemoveOwnersEvent = TypedDict('RemoveOwnersEvent', {
	'owners_removed': List['Address'],
})


RequestCommissionEvent = TypedDict('RequestCommissionEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
	'accumulated_rewards': 'U64',
	'commission_amount': 'U64',
})


ResolveProposal = TypedDict('ResolveProposal', {
	'proposal_id': 'U64',
	'yes_votes': 'U128',
	'no_votes': 'U128',
	'resolved_early': bool,
})


Result = TypedDict('Result', {
	'inner': 'U8',
})


RistrettoPoint = TypedDict('RistrettoPoint', {
	'handle': 'U64',
})


RotateConsensusKeyEvent = TypedDict('RotateConsensusKeyEvent', {
	'pool_address': 'Address',
	'old_consensus_pubkey': List['U8'],
	'new_consensus_pubkey': List['U8'],
})


RotationCapability = TypedDict('RotationCapability', {
	'account': 'Address',
})


RotationCapabilityOfferProofChallenge = TypedDict('RotationCapabilityOfferProofChallenge', {
	'sequence_number': 'U64',
	'recipient_address': 'Address',
})


RotationCapabilityOfferProofChallengeV2 = TypedDict('RotationCapabilityOfferProofChallengeV2', {
	'chain_id': 'U8',
	'sequence_number': 'U64',
	'source_address': 'Address',
	'recipient_address': 'Address',
})


RotationProofChallenge = TypedDict('RotationProofChallenge', {
	'sequence_number': 'U64',
	'originator': 'Address',
	'current_auth_key': 'Address',
	'new_public_key': List['U8'],
})


Scalar = TypedDict('Scalar', {
	'data': List['U8'],
})


SetBeneficiaryEvent = TypedDict('SetBeneficiaryEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'shareholder': 'Address',
	'old_beneficiary': 'Address',
	'new_beneficiary': 'Address',
})


SetOperatorEvent = TypedDict('SetOperatorEvent', {
	'pool_address': 'Address',
	'old_operator': 'Address',
	'new_operator': 'Address',
})


SetVersionCapability = TypedDict('SetVersionCapability', {
	'dummy_field': bool,
})


SignedMessage = TypedDict('SignedMessage', {
	'type_info': 'TypeInfo',
	'inner': 'Any',
})


SignerCapability = TypedDict('SignerCapability', {
	'account': 'Address',
})


SignerCapabilityOfferProofChallenge = TypedDict('SignerCapabilityOfferProofChallenge', {
	'sequence_number': 'U64',
	'recipient_address': 'Address',
})


SignerCapabilityOfferProofChallengeV2 = TypedDict('SignerCapabilityOfferProofChallengeV2', {
	'sequence_number': 'U64',
	'source_address': 'Address',
	'recipient_address': 'Address',
})


SimpleMap = TypedDict('SimpleMap', {
	'data': List['_0x0000000000000000000000000000000000000000000000000000000000000001__simple_map__Element'],
})


SmartTable = TypedDict('SmartTable', {
	'buckets': 'TableWithLength',
	'num_buckets': 'U64',
	'level': 'U8',
	'size': 'U64',
	'split_load_threshold': 'U8',
	'target_bucket_size': 'U64',
})


SmartVector = TypedDict('SmartVector', {
	'inline_vec': List['Any'],
	'big_vec': 'Option',
	'inline_capacity': 'Option',
	'bucket_size': 'Option',
})


StakePool = TypedDict('StakePool', {
	'active': 'Coin',
	'inactive': 'Coin',
	'pending_active': 'Coin',
	'pending_inactive': 'Coin',
	'locked_until_secs': 'U64',
	'operator_address': 'Address',
	'delegated_voter': 'Address',
	'initialize_validator_events': 'EventHandle',
	'set_operator_events': 'EventHandle',
	'add_stake_events': 'EventHandle',
	'reactivate_stake_events': 'EventHandle',
	'rotate_consensus_key_events': 'EventHandle',
	'update_network_and_fullnode_addresses_events': 'EventHandle',
	'increase_lockup_events': 'EventHandle',
	'join_validator_set_events': 'EventHandle',
	'distribute_rewards_events': 'EventHandle',
	'unlock_stake_events': 'EventHandle',
	'withdraw_stake_events': 'EventHandle',
	'leave_validator_set_events': 'EventHandle',
})


StakingConfig = TypedDict('StakingConfig', {
	'minimum_stake': 'U64',
	'maximum_stake': 'U64',
	'recurring_lockup_duration_secs': 'U64',
	'allow_validator_set_change': bool,
	'rewards_rate': 'U64',
	'rewards_rate_denominator': 'U64',
	'voting_power_increase_limit': 'U64',
})


StakingContract = TypedDict('StakingContract', {
	'principal': 'U64',
	'pool_address': 'Address',
	'owner_cap': 'OwnerCapability',
	'commission_percentage': 'U64',
	'distribution_pool': '_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64__Pool',
	'signer_cap': 'SignerCapability',
})


StakingGroupContainer = TypedDict('StakingGroupContainer', {
	'dummy_field': bool,
})


StakingGroupUpdateCommissionEvent = TypedDict('StakingGroupUpdateCommissionEvent', {
	'update_commission_events': 'EventHandle',
})


StakingInfo = TypedDict('StakingInfo', {
	'pool_address': 'Address',
	'operator': 'Address',
	'voter': 'Address',
	'commission_percentage': 'U64',
})


StakingRewardsConfig = TypedDict('StakingRewardsConfig', {
	'rewards_rate': 'FixedPoint64',
	'min_rewards_rate': 'FixedPoint64',
	'rewards_rate_period_in_secs': 'U64',
	'last_rewards_rate_period_start_in_secs': 'U64',
	'rewards_rate_decrease_rate': 'FixedPoint64',
})


StateStorageUsage = TypedDict('StateStorageUsage', {
	'epoch': 'U64',
	'usage': 'Usage',
})


StorageGas = TypedDict('StorageGas', {
	'per_item_read': 'U64',
	'per_item_create': 'U64',
	'per_item_write': 'U64',
	'per_byte_read': 'U64',
	'per_byte_create': 'U64',
	'per_byte_write': 'U64',
})


StorageGasConfig = TypedDict('StorageGasConfig', {
	'item_config': 'UsageGasConfig',
	'byte_config': 'UsageGasConfig',
})


Store = TypedDict('Store', {
	'staking_contracts': 'SimpleMap',
	'create_staking_contract_events': 'EventHandle',
	'update_voter_events': 'EventHandle',
	'reset_lockup_events': 'EventHandle',
	'add_stake_events': 'EventHandle',
	'request_commission_events': 'EventHandle',
	'unlock_stake_events': 'EventHandle',
	'switch_operator_events': 'EventHandle',
	'add_distribution_events': 'EventHandle',
	'distribute_events': 'EventHandle',
})


Supply = TypedDict('Supply', {
	'current': 'U128',
	'maximum': 'Option',
})


SupplyConfig = TypedDict('SupplyConfig', {
	'allow_upgrades': bool,
})


SwitchOperatorEvent = TypedDict('SwitchOperatorEvent', {
	'old_operator': 'Address',
	'new_operator': 'Address',
	'pool_address': 'Address',
})


Table = TypedDict('Table', {
	'handle': 'Address',
})


TableWithLength = TypedDict('TableWithLength', {
	'inner': 'Table',
	'length': 'U64',
})


TerminateEvent = TypedDict('TerminateEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
})


TransactionExecutionFailedEvent = TypedDict('TransactionExecutionFailedEvent', {
	'executor': 'Address',
	'sequence_number': 'U64',
	'transaction_payload': List['U8'],
	'num_approvals': 'U64',
	'execution_error': 'ExecutionError',
})


TransactionExecutionSucceededEvent = TypedDict('TransactionExecutionSucceededEvent', {
	'executor': 'Address',
	'sequence_number': 'U64',
	'transaction_payload': List['U8'],
	'num_approvals': 'U64',
})


TransactionValidation = TypedDict('TransactionValidation', {
	'module_addr': 'Address',
	'module_name': List['U8'],
	'script_prologue_name': List['U8'],
	'module_prologue_name': List['U8'],
	'multi_agent_prologue_name': List['U8'],
	'user_epilogue_name': List['U8'],
})


TransferEvent = TypedDict('TransferEvent', {
	'object': 'Address',
	'from': 'Address',
	'to': 'Address',
})


TypeInfo = TypedDict('TypeInfo', {
	'account_address': 'Address',
	'module_name': List['U8'],
	'struct_name': List['U8'],
})


UnlockRewardsEvent = TypedDict('UnlockRewardsEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'staking_pool_address': 'Address',
	'amount': 'U64',
})


UpdateCommissionEvent = TypedDict('UpdateCommissionEvent', {
	'staker': 'Address',
	'operator': 'Address',
	'old_commission_percentage': 'U64',
	'new_commission_percentage': 'U64',
})


UpdateConfigEvent = TypedDict('UpdateConfigEvent', {
	'min_voting_threshold': 'U128',
	'required_proposer_stake': 'U64',
	'voting_duration_secs': 'U64',
})


UpdateEpochIntervalEvent = TypedDict('UpdateEpochIntervalEvent', {
	'old_epoch_interval': 'U64',
	'new_epoch_interval': 'U64',
})


UpdateNetworkAndFullnodeAddressesEvent = TypedDict('UpdateNetworkAndFullnodeAddressesEvent', {
	'pool_address': 'Address',
	'old_network_addresses': List['U8'],
	'new_network_addresses': List['U8'],
	'old_fullnode_addresses': List['U8'],
	'new_fullnode_addresses': List['U8'],
})


UpdateOperatorEvent = TypedDict('UpdateOperatorEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'staking_pool_address': 'Address',
	'old_operator': 'Address',
	'new_operator': 'Address',
	'commission_percentage': 'U64',
})


UpdateSignaturesRequiredEvent = TypedDict('UpdateSignaturesRequiredEvent', {
	'old_num_signatures_required': 'U64',
	'new_num_signatures_required': 'U64',
})


UpgradePolicy = TypedDict('UpgradePolicy', {
	'policy': 'U8',
})


Usage = TypedDict('Usage', {
	'items': 'U64',
	'bytes': 'U64',
})


UsageGasConfig = TypedDict('UsageGasConfig', {
	'target_usage': 'U64',
	'read_curve': 'GasCurve',
	'create_curve': 'GasCurve',
	'write_curve': 'GasCurve',
})


ValidatorConfig = TypedDict('ValidatorConfig', {
	'consensus_pubkey': List['U8'],
	'network_addresses': List['U8'],
	'fullnode_addresses': List['U8'],
	'validator_index': 'U64',
})


ValidatorConfiguration = TypedDict('ValidatorConfiguration', {
	'owner_address': 'Address',
	'operator_address': 'Address',
	'voter_address': 'Address',
	'stake_amount': 'U64',
	'consensus_pubkey': List['U8'],
	'proof_of_possession': List['U8'],
	'network_addresses': List['U8'],
	'full_node_network_addresses': List['U8'],
})


ValidatorConfigurationWithCommission = TypedDict('ValidatorConfigurationWithCommission', {
	'validator_config': 'ValidatorConfiguration',
	'commission_percentage': 'U64',
	'join_during_genesis': bool,
})


ValidatorFees = TypedDict('ValidatorFees', {
	'fees_table': 'Table',
})


ValidatorInfo = TypedDict('ValidatorInfo', {
	'addr': 'Address',
	'voting_power': 'U64',
	'config': 'ValidatorConfig',
})


ValidatorPerformance = TypedDict('ValidatorPerformance', {
	'validators': List['IndividualValidatorPerformance'],
})


ValidatorSet = TypedDict('ValidatorSet', {
	'consensus_scheme': 'U8',
	'active_validators': List['ValidatorInfo'],
	'pending_inactive': List['ValidatorInfo'],
	'pending_active': List['ValidatorInfo'],
	'total_voting_power': 'U128',
	'total_joining_power': 'U128',
})


Vegetable = TypedDict('Vegetable', {
	'name': str,
	'energy_joules': 'U64',
	'fibre_grams': 'U64',
	'aesthetic_profile': 'AestheticProfile',
})


Version = TypedDict('Version', {
	'major': 'U64',
})


VestEvent = TypedDict('VestEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'staking_pool_address': 'Address',
	'period_vested': 'U64',
	'amount': 'U64',
})


VestingAccountManagement = TypedDict('VestingAccountManagement', {
	'roles': 'SimpleMap',
})


VestingContract = TypedDict('VestingContract', {
	'state': 'U64',
	'admin': 'Address',
	'grant_pool': '_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64__Pool',
	'beneficiaries': 'SimpleMap',
	'vesting_schedule': 'VestingSchedule',
	'withdrawal_address': 'Address',
	'staking': 'StakingInfo',
	'remaining_grant': 'U64',
	'signer_cap': 'SignerCapability',
	'update_operator_events': 'EventHandle',
	'update_voter_events': 'EventHandle',
	'reset_lockup_events': 'EventHandle',
	'set_beneficiary_events': 'EventHandle',
	'unlock_rewards_events': 'EventHandle',
	'vest_events': 'EventHandle',
	'distribute_events': 'EventHandle',
	'terminate_events': 'EventHandle',
	'admin_withdraw_events': 'EventHandle',
})


VestingSchedule = TypedDict('VestingSchedule', {
	'schedule': List['FixedPoint32'],
	'start_timestamp_secs': 'U64',
	'period_duration': 'U64',
	'last_vested_period': 'U64',
})


VoteDelegation = TypedDict('VoteDelegation', {
	'voter': 'Address',
	'pending_voter': 'Address',
	'last_locked_until_secs': 'U64',
})


VotingEvents = TypedDict('VotingEvents', {
	'create_proposal_events': 'EventHandle',
	'register_forum_events': 'EventHandle',
	'resolve_proposal_events': 'EventHandle',
	'vote_events': 'EventHandle',
})


VotingForum = TypedDict('VotingForum', {
	'proposals': 'Table',
	'events': 'VotingEvents',
	'next_proposal_id': 'U64',
})


VotingRecordKey = TypedDict('VotingRecordKey', {
	'voter': 'Address',
	'proposal_id': 'U64',
})


VotingRecords = TypedDict('VotingRecords', {
	'votes': 'Table',
})


VotingRecordsV2 = TypedDict('VotingRecordsV2', {
	'votes': 'SmartTable',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__any__Any = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__any__Any', {
	'type_name': str,
	'data': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__aptos_governance__CreateProposalEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__aptos_governance__CreateProposalEvent', {
	'proposer': 'Address',
	'stake_pool': 'Address',
	'proposal_id': 'U64',
	'execution_hash': List['U8'],
	'proposal_metadata': 'SimpleMap',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__aptos_governance__VoteEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__aptos_governance__VoteEvent', {
	'proposal_id': 'U64',
	'voter': 'Address',
	'stake_pool': 'Address',
	'num_votes': 'U64',
	'should_pass': bool,
})


_0x0000000000000000000000000000000000000000000000000000000000000001__bls12381__Signature = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__bls12381__Signature', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__coin__DepositEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__coin__DepositEvent', {
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__coin__WithdrawEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__coin__WithdrawEvent', {
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__copyable_any__Any = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__copyable_any__Any', {
	'type_name': str,
	'data': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__crypto_algebra__Element = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__crypto_algebra__Element', {
	'handle': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__AddStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__AddStakeEvent', {
	'pool_address': 'Address',
	'delegator_address': 'Address',
	'amount_added': 'U64',
	'add_stake_fee': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__CreateProposalEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__CreateProposalEvent', {
	'proposal_id': 'U64',
	'voter': 'Address',
	'delegation_pool': 'Address',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__ReactivateStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__ReactivateStakeEvent', {
	'pool_address': 'Address',
	'delegator_address': 'Address',
	'amount_reactivated': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__UnlockStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__UnlockStakeEvent', {
	'pool_address': 'Address',
	'delegator_address': 'Address',
	'amount_unlocked': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__VoteEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__VoteEvent', {
	'voter': 'Address',
	'proposal_id': 'U64',
	'delegation_pool': 'Address',
	'num_votes': 'U64',
	'should_pass': bool,
})


_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__WithdrawStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__delegation_pool__WithdrawStakeEvent', {
	'pool_address': 'Address',
	'delegator_address': 'Address',
	'amount_withdrawn': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__ed25519__Signature = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__ed25519__Signature', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__ed25519__UnvalidatedPublicKey = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__ed25519__UnvalidatedPublicKey', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__ed25519__ValidatedPublicKey = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__ed25519__ValidatedPublicKey', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__fungible_asset__DepositEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__fungible_asset__DepositEvent', {
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__fungible_asset__TransferRef = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__fungible_asset__TransferRef', {
	'metadata': 'Object',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__fungible_asset__WithdrawEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__fungible_asset__WithdrawEvent', {
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__guid__ID = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__guid__ID', {
	'creation_num': 'U64',
	'addr': 'Address',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__multi_ed25519__Signature = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__multi_ed25519__Signature', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__multi_ed25519__UnvalidatedPublicKey = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__multi_ed25519__UnvalidatedPublicKey', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__multi_ed25519__ValidatedPublicKey = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__multi_ed25519__ValidatedPublicKey', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__multisig_account__VoteEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__multisig_account__VoteEvent', {
	'owner': 'Address',
	'sequence_number': 'U64',
	'approved': bool,
})


_0x0000000000000000000000000000000000000000000000000000000000000001__object__TransferRef = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__object__TransferRef', {
	'self': 'Address',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64__Pool = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64__Pool', {
	'shareholders_limit': 'U64',
	'total_coins': 'U64',
	'total_shares': 'U64',
	'shares': 'SimpleMap',
	'shareholders': List['Address'],
	'scaling_factor': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64_unbound__Pool = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__pool_u64_unbound__Pool', {
	'total_coins': 'U64',
	'total_shares': 'U128',
	'shares': 'TableWithLength',
	'scaling_factor': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__simple_map__Element = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__simple_map__Element', {
	'key': 'Any',
	'value': 'Any',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__stake__AddStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__stake__AddStakeEvent', {
	'pool_address': 'Address',
	'amount_added': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__stake__AptosCoinCapabilities = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__stake__AptosCoinCapabilities', {
	'mint_cap': 'MintCapability',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__stake__ReactivateStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__stake__ReactivateStakeEvent', {
	'pool_address': 'Address',
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__stake__UnlockStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__stake__UnlockStakeEvent', {
	'pool_address': 'Address',
	'amount_unlocked': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__stake__WithdrawStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__stake__WithdrawStakeEvent', {
	'pool_address': 'Address',
	'amount_withdrawn': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__AddStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__AddStakeEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__DistributeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__DistributeEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
	'recipient': 'Address',
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__ResetLockupEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__ResetLockupEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__UnlockStakeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__UnlockStakeEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
	'amount': 'U64',
	'commission_paid': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__UpdateVoterEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__staking_contract__UpdateVoterEvent', {
	'operator': 'Address',
	'pool_address': 'Address',
	'old_voter': 'Address',
	'new_voter': 'Address',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__string__String = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__string__String', {
	'bytes': List['U8'],
})


_0x0000000000000000000000000000000000000000000000000000000000000001__transaction_fee__AptosCoinCapabilities = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__transaction_fee__AptosCoinCapabilities', {
	'burn_cap': 'BurnCapability',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__vesting__DistributeEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__vesting__DistributeEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'amount': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__vesting__ResetLockupEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__vesting__ResetLockupEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'staking_pool_address': 'Address',
	'new_lockup_expiration_secs': 'U64',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__vesting__UpdateVoterEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__vesting__UpdateVoterEvent', {
	'admin': 'Address',
	'vesting_contract_address': 'Address',
	'staking_pool_address': 'Address',
	'old_voter': 'Address',
	'new_voter': 'Address',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__voting__CreateProposalEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__voting__CreateProposalEvent', {
	'proposal_id': 'U64',
	'early_resolution_vote_threshold': 'Option',
	'execution_hash': List['U8'],
	'expiration_secs': 'U64',
	'metadata': 'SimpleMap',
	'min_vote_threshold': 'U128',
})


_0x0000000000000000000000000000000000000000000000000000000000000001__voting__VoteEvent = TypedDict('_0x0000000000000000000000000000000000000000000000000000000000000001__voting__VoteEvent', {
	'proposal_id': 'U64',
	'num_votes': 'U64',
})


