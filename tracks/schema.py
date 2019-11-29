import graphene
from graphene_django import DjangoObjectType
from .models import Tracks


class TrackType(DjangoObjectType):
    class Meta:
        model = Tracks


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)



    def resolve_tracks(self, info):
        return Tracks.objects.all()


class CreateTrack(graphene.Mutation):
    '''
    class to create a track
    '''
    track = graphene.Field(TrackType)


    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()


    def mutate(self, info, title, description, url):
        user = info.context.user

        if user.is_anonymous:
            raise Exception("Log in to add a track.")

        track = Tracks(title=title, description=description, url=url, posted_by=user)
        track.save()

        return CreateTrack(track=track)


class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)


    class Arguments:
        track_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()


    def mutate(self, info, track_id, title, description, url):

        user = info.context.user
        track = Tracks.objects.get(id=track_id)

        if track.posted_by != user:
            raise Exception("Not permitted to update this track.")

        track.title = title
        track.description = description
        track.url = url

        track.save()

        return UpdateTrack(track=track)


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()